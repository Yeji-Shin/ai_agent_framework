import torch
from typing import List

from langchain_community.embeddings import HuggingFaceEmbeddings


def get_embeddings_model(texts: List, model_name: str="jhgan/ko-sroberta-nli", batch_size: int=32) -> List:
    """Hugging Face 모델을 이용하여 텍스트를 임베딩 벡터로 변환하는 함수

    Args:
        texts (List): 임베딩할 텍스트 리스트
        model_name (str, optional): 사용할 모델 이름. Defaults to "jhgan/ko-sroberta-nli".
        batch_size (int, optional): batch size. Defaults to 32.

    Returns:
        List: 생성된 임베딩 벡터 리스트
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"

    embeddings_model = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={'device':device},
        encode_kwargs={'normalize_embeddings':True, 'batch_size': batch_size}
    )

    return embeddings_model