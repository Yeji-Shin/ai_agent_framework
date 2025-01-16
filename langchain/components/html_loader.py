from typing import List

from langchain_community.document_loaders import UnstructuredHTMLLoader


def load_html(url_path: str) -> List:
    """Langchain의 UnstructuredHTMLLoader를 사용하여 machine readable한 형태로 변환
    이후 문단 나누기와 임베딩을 위한 수행 작업

    Args:
        url_path (str): _description_

    Returns:
        List: Document 객체들의 리스트, page_content 속성으로 텍스트 내용 확인
    """
    loader = UnstructuredHTMLLoader(url_path)
    document_data = loader.load()
    return document_data