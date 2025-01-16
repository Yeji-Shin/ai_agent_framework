def increment(state):
    """현재 graph state를 받아서 state의 counter 값을 1 증가시킨 새로운 상태를 반환

    Args:
        state (_type_): graph state

    Returns:
        Dict: new state
    """
    return {"counter": state["counter"] + 1}