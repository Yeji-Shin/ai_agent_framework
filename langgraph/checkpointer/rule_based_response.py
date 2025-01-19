def generate_response(user_message):
    """룰 기반으로 시스템 응답을 생성합니다."""
    user_message = user_message.lower()
    if ("안녕" or "안녕하세요") in user_message:
        return "안녕하세요! 어떻게 도와드릴까요?"
    elif "날씨" in user_message:
        return "오늘의 날씨는 맑고 기온은 20도입니다."
    elif "이름" in user_message:
        return "저는 챗봇입니다!"
    else:
        return "죄송합니다, 이해하지 못했습니다. 다시 질문해주세요."