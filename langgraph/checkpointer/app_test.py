import streamlit as st

from memory_saver import ConditionalMemorySaver
from state_manager import rollback_state, optimize_state
from langgraph.graph import StateGraph, START
from rule_based_response import generate_response
from states import State

# 상태를 수동으로 관리하는 예시
checkpoint_history = []

def handle_user_message(graph, user_message, user_id):
    """사용자가 메시지를 보낸 후, 시스템의 응답을 처리합니다."""
    config = {"configurable": {"thread_id": user_id}}

    # 사용자 메시지를 시스템에 전달하여 응답 받기
    try:
        # 랭그래프에 메시지 추가
        graph.invoke(
            {
                "messages": [{"role": "user", "content": user_message}],
                "context": f"user_id:{user_id}"
            },
            config=config)
        
        # 시스템 응답 생성
        system_response = generate_response(user_message=user_message)
        print(system_response)

        # 메시지 상태를 업데이트
        current_state = graph.get_state(config).values
        current_state["messages"].append(
            {"role": "user", "content": user_message})
        current_state["messages"].append(
            {"role": "system", "content": system_response})
        print(current_state)

        # 최근 10개의 메세지만 유지
        optimized_state = optimize_state(current_state)

        # 상태를 수동으로 기록 (체크포인트 기록)
        checkpoint_history.append(optimized_state)

        graph.update_state(config, optimized_state)
        return system_response

    except Exception as e:
        rollback_state(graph, config, checkpoint_history)
        return f"에러가 발생하여 상태를 롤백했습니다: {e}"

# 2개의 메세지 마다 체크포인트 생성
def is_checkpoint(state) -> bool:
    return len(state['messages']) % 2 == 0

# # 사람의 리뷰 또는 수정 로직
# def human_review_needed(state):
#     if state.values.get('confidence_score', 0) < 0.7:
#         raise NodeInterrupt("인간 검토 필요")
#     return state

# Streamlit 인터페이스
st.title("대화형 챗봇")

# 사용자 ID 설정 (thread_id)
user_id = st.text_input("사용자 ID를 입력하세요:", value="user_1")

# 사용자 메시지 입력
user_message = st.text_area("메시지를 입력하세요:", key="user_message")

# StateGraph 생성 후 체크포인트 설정
workflow = StateGraph(State)  # StateGraph 객체 생성
workflow.add_node("handle_user_message", handle_user_message)
# workflow.add_node("human_review", human_review_needed)

workflow.add_edge(START, "handle_user_message")
# workflow.add_edge("handle_user_message", "human_review")
# workflow.add_edge("human_review", "handle_user_message")


memory_saver = ConditionalMemorySaver(is_checkpoint)  # MemorySaver 인스턴스 생성
graph = workflow.compile(checkpointer=memory_saver)  # 체크포인터 추가
print(graph)


# 대화 시작 또는 계속
if st.button("전송"):
    if user_message.strip():
        try:
            response = handle_user_message(graph, user_message, user_id)
            st.write(f"시스템 응답: {response}")
        except Exception as e:
            # 에러 발생 시 상세 정보 출력
            print(f"Error occurred: {e}")
            # 에러 처리 로직 추가 (예: 로그 기록, 사용자에게 알림)