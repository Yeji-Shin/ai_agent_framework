from typing import Optional, TypedDict

class WeatherState(TypedDict):
    """그래프의 각 단계에서 사용되는 데이터 구조 정의

    query: 사용자의 원래 질문
    location: 추출된 위치 정보
    forecast: 가져온 날씨 예보 정보
    """
    query: str
    location: Optional[str]
    forecast: Optional[str]
