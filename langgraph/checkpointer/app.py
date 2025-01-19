import streamlit as st
from states import State
from utils import create_conversation, rollback_state, get_conversation_history
from memory_saver import optimize_state

# 대화 초기화
graph = create_conversation(State)

# Streamlit 인터페이스
st.title("대화형 챗봇")

# 사용자 ID 설정 (thread_id)
user_id = st.text_input("사용자 ID를 입력하세요:", value="user_1")

# 세션 상태 초기화
if "state" not in st.session_state:
    st.session_state["state"] = State(messages=[], context="")
if "graph" not in st.session_state:
    st.session_state["graph"] = create_conversation(st.session_state["state"])

# 대화 내용 표시
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 대화 표시
st.subheader("대화 히스토리")
if "messages" in st.session_state["state"]:
    # 이전 대화 내용 표시
    for msg in st.session_state["messages"]:
        if msg['role'] == 'user':
            st.markdown(f"**사용자**: {msg['content']}")
        else:
            st.markdown(f"**시스템**: {msg['content']}")

# 사용자 메시지 입력
user_message = st.text_area("메시지를 입력하세요:", key="user_message")

# 대화 시작 또는 계속
if st.button("전송"):
    if user_message.strip():
        # 사용자 메시지 추가
        st.session_state["messages"].append(
            {"role": "user", "content": user_message})

        # 그래프를 통해 응답 처리
        try:
            system_response = handle_user_message(
                st.session_state["graph"], 
                user_message, 
                user_id
            )
            # 챗봇 응답 추가
            st.session_state["state"]["messages"].append({"role": "system", "content": system_response})
        except Exception as e:
            st.error(f"에러 발생: {e}")

# 상태 롤백
if st.button("롤백"):
    try:
        rollback_state = st.session_state["graph"].rollback({"configurable": {"thread_id": user_id}})
        st.session_state["state"] = rollback_state
        st.success("상태가 마지막 체크포인트로 롤백되었습니다.")
    except Exception as e:
        st.error(f"롤백 실패: {e}")

# 대화 상태 확인
if st.checkbox("현재 상태 확인"):
    st.json(st.session_state["state"])

# 대화 히스토리 확인
if st.checkbox("대화 히스토리 보기"):
    history = get_conversation_history(st.session_state["graph"], user_id)
    st.write("대화 히스토리:", history)
#         # # 대화 진행
#         # config = {"configurable": {"thread_id": user_id}}
#         # response = graph.invoke(
#         #     {"messages": [{"role": "user", "content": user_message}], "context": ""},
#         #     config=config)
        
#         # # 시스템 응답 저장
#         # system_response = response.get("content", "응답을 생성할 수 없습니다.")
#         # st.session_state["messages"].append(
#         #     {"role": "system", "content": system_response})

#         # 상태 최적화
#         current_state = graph.get_state(config).values
#         optimized_state = optimize_state(current_state)
#         graph.update_state(config, optimized_state)

#         # 대화 히스토리 저장
#         st.session_state["messages"].append(
#             {"role": "system", "content": "새로운 메시지가 추가되었습니다."})

# # 상태를 최신으로 업데이트
# if st.button("상태 확인"):
#     config = {"configurable": {"thread_id": user_id}}
#     current_state = graph.get_state(config).values
#     st.write("현재 상태:", current_state)
