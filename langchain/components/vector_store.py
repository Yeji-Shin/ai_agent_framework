from typing import List

from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy


class FaissVectorStore:
    def __init__(self, embedding_model: str):
        self.embedding_model = embedding_model
        self.vector_store = None

    def create(self, texts: List[str], distance_strategy=DistanceStrategy.COSINE):
        """벡터 스토어 생성

        Args:
            texts (List[str]): 임베딩할 텍스트 데이터 리스트
            distance_strategy (DistanceStrategy, optional): 거리 측정 전략. Defaults to DistanceStrategy.COSINE.
        """
        self.vector_store = FAISS.from_documents(
            texts,
            embedding=self.embedding_model,
            distance_strategy=distance_strategy
        )

    def save(self, save_path: str):
        """벡터 스토어 저장

        Args:
            save_path (str): 저장 경로
        """
        self.vector_store.save_local(save_path)

    def load(self, index_url: str, allow_dangerous_deserialization=False):
        """벡터 스토어 로드

        Args:
            index_url (str): 인덱스 파일 경로
            allow_dangerous_deserialization (bool, optional): 위험한 역직렬화 허용 여부. Defaults to False.
        """
        self.loaded_vector_store = FAISS.load_local(index_url, self.embedding_model, allow_dangerous_deserialization=allow_dangerous_deserialization)
        return self.loaded_vector_store

    def similarity_search(self, query: str, k: int = 4):
        """유사도 검색 (retriever 역할)

        Args:
            query (str): 쿼리 문장
            k (int, optional): 상위 k개의 결과를 반환. Defaults to 4.

        Returns:
            List: 유사도가 높은 문서들의 인덱스 리스트
        """
        retriever = self.vector_store.as_retriever(search_kwargs={'k': k})
        docs = retriever.get_relevant_documents(query)
        return docs