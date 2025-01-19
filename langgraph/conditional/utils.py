from typing import Literal, Optional, TypedDict

def extract_location(query: str) -> Optional[str]:
    """쿼리에서 "in" 다음에 오는 단어를 위치로 간주

    Args:
        query (str): 사용자의 질의

    Returns:
        Optional[str]: location
    """
    words = query.split()
    if "날씨" in words:
        index = words.index("날씨")
        if index > 0:
            return words[index - 1]
    return None

def is_ambiguous(location: str) -> bool:
    """location 이 명확한지 확인

    Args:
        location (str): location

    Returns:
        bool: 위치가 1글자 미만이면 애매한 것으로 간주
    """
    return len(location) <= 1

def fetch_weather_data(location: str) -> str:
    """주어진 위치에 대한 날씨 정보를 제공

    Args:
        location (str): location

    Returns:
        str: weather
    """
    weather_data = {  # 간단한 모의 날씨 데이터
        "서울": "Sunny, 25°C",
        "부산": "Rainy, 15°C",
        "대구": "Cloudy, 20°C",
        "뉴욕": "Partly cloudy, 22°C"
    }
    return weather_data.get(location, "Weather data not available")

def generate_location_clarification(location: str) -> str:
    """모호한 위치에 대해 사용자에게 추가 정보를 요청

    Args:
        location (str): location

    Returns:
        str: message
    """
    return f"Could you please provide more details about the location '{location}'?"

def format_weather_response(location: str, forecast: str) -> str:
    """최종 날씨 정보 응답을 생성

    Args:
        location (str): location
        forecast (str): forecast

    Returns:
        str: weather description
    """
    return f"The weather in {location} is: {forecast}"
