from typing import TypedDict

class MyState(TypedDict):
    counter: int
    """여기서 '상태'는 단순히 숫자를 세는 카운터

    TypedDict는 딕셔너리의 키와 값의 타입을 미리 정의할 수 있게 해주는 도구
    - counter 라는 키에 정수형 값이 들어가야 함
    """
