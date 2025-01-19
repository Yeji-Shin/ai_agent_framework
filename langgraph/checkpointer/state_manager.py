def optimize_state(state):
    """최근 10개의 메세지만 유지 (에러 처리를 위함)"""
    state['messages'] = state['messages'][-10:]
    return state

def rollback_state(graph, config, checkpoint_history):
    """마지막 체크포인트로 상태를 롤백합니다."""
    try:
        # 히스토리에서 마지막 상태 가져오기
        if checkpoint_history:
            last_checkpoint = checkpoint_history[-1]  # 가장 최근 상태로 롤백
            graph.update_state(config, last_checkpoint)
            return last_checkpoint
        else:
            raise ValueError("롤백 가능한 상태가 없습니다.")
    except Exception as e:
        raise RuntimeError(f"상태 롤백 중 오류 발생: {e}")
