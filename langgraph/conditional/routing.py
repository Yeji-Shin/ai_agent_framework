from typing import Literal
from state import WeatherState
from utils import is_ambiguous

def check_location(state: WeatherState) -> Literal["valid", "invalid", "ambiguous"]:
    """위치 정보의 상태에 따라 다음 세 가지 결과 중 하나를 반환

    Returns:
        _type_: "valid": 유효한 위치일 경우
                "invalid": 위치 정보가 없는 경우
                "ambiguous": 위치 정보가 모호한 경우
    """
    if not state["location"]:
        return "invalid"
    elif is_ambiguous(state["location"]):
        return "ambiguous"
    else:
        return "valid"
