from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter


def create_recursive_text_splitter(chunk_size: int = 1000, chunk_overlap: int = 0) -> RecursiveCharacterTextSplitter:
    """텍스트 스플리터를 생성합니다.
    - 텍스트를 재귀적으로 분할하여 의미적으로 관련 있는 텍스트 조각들이 같이 있도록 하는 목적으로 설계
    - 문자 리스트(['\n\n', '\n', ' ', ''])의 문자를 순서대로 사용하여 텍스트를 분할하며,
    - 분할된 청크들이 설정된 chunk_size보다 작아질 때까지 이 과정을 반복

    Args:
        chunk_size: 각 청크의 최대 길이
        chunk_overlap: 청크 간 겹치는 부분의 길이

    Returns:
        RecursiveCharacterTextSplitter: 생성된 텍스트 스플리터
    """

    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

def create_text_splitter(seperator: str = '', chunk_size: int = 1000, chunk_overlap: int = 0) -> CharacterTextSplitter:
    """텍스트 스플리터를 생성합니다.

    Args:
        seperator: 텍스트 분할 기준
        chunk_size: 각 청크의 최대 길이
        chunk_overlap: 청크 간 겹치는 부분의 길이

    Returns:
        CharacterTextSplitter: 생성된 텍스트 스플리터
    """

    return CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )