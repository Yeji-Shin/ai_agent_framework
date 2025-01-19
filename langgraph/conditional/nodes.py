from utils import *
from state import WeatherState

# 각 노드는 상태를 입력으로 받아 상태의 일부를 업데이트

def parse_query(state: WeatherState):
    """사용자 쿼리에서 위치 정보를 추출

    Args:
        state (WeatherState): WeatherState

    Returns:
        _type_: location
    """
    location = extract_location(state["query"])
    return {"location": location}

def get_forecast(state: WeatherState):
    """주어진 위치에 대한 날씨 정보를 추출

    Args:
        state (WeatherState): WeatherState

    Returns:
        _type_: forecast
    """
    forecast = fetch_weather_data(state["location"])
    return {"forecast": forecast}

def clarify_location(state: WeatherState):
    """위치가 모호할 경우 명확화 요청을 생성

    Args:
        state (WeatherState): WeatherState

    Returns:
        _type_: query
    """
    clarification = generate_location_clarification(state["location"])
    return {"query": clarification}

def generate_response(state: WeatherState):
    """최종 응답을 생성

    Args:
        state (WeatherState): WeatherState

    Returns:
        _type_: response
    """
    response = format_weather_response(state["location"], state["forecast"])
    return {"response": response}
