from langgraph.graph import StateGraph, START, END
from state import WeatherState
from nodes import *
from routing import check_location


# 1. StateGraph 객체를 생성하여 그래프의 기본 구조를 정의합니다.
conditional_graph = StateGraph(WeatherState)

# 2. add_node로 각 처리 단계(노드)를 그래프에 추가합니다.
conditional_graph.add_node("parse_query", parse_query)
conditional_graph.add_node("get_forecast", get_forecast)
conditional_graph.add_node("clarify_location", clarify_location)
conditional_graph.add_node("generate_response", generate_response)

# 3. set_entry_point로 그래프의 시작점을 설정합니다.
conditional_graph.set_entry_point("parse_query")

# 4. add_conditional_edges로 조건부 라우팅을 정의합니다.
"""
- "parse_query" 라는 노드에서 나오는 WeatherState의 location 의 상태에 따라 다른 노드로 연결되도록 함
- check_location 함수를 통해 state 에 따른 분기 처리
- 결과값에 따라 get_forecast 또는 clarify_location 노드에 연결
- 이전 Node에서 전달하는 특정 State가 라우팅의 '키' 가 된다
"""
conditional_graph.add_conditional_edges(
    "parse_query",
    check_location,
    {
        "valid": "get_forecast",
        "ambiguous": "clarify_location",
        "invalid": END
    }
)

# 5. add_edge로 일반적인 순차적 처리 흐름을 정의합니다.
conditional_graph.add_edge("clarify_location", "parse_query") # 사용자개 새로운 입력 제공
conditional_graph.add_edge("get_forecast", "generate_response")
conditional_graph.add_edge("generate_response", END)

# 6. compile로 정의된 그래프를 실행 가능한 형태로 변환합니다.
app = conditional_graph.compile()
