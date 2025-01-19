from typing import TypedDict, List

class State(TypedDict):
    messages: List[str]
    context: str
