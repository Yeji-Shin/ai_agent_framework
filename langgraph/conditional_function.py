from typing import Literal


def check_user_input(state) -> Literal["question", "command", "unknown"]:
    """현재 상태를 평가하고 다음에 어떤 노드로 이동할지 결정

    Returns:
        _type_: 입력이 물음표로 끝나면 "question"을 반환합니다.
                입력이 느낌표로 시작하면 "command"를 반환합니다.
                그 외의 경우 "unknown"을 반환합니다.
    """
    user_input = state["user_input"].lower()

    if user_input.endswith("?"):
        return "question"
    elif user_input.startswith("!"):
        return "command"
    else:
        return "unknown"
