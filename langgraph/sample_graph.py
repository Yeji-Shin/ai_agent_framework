import graphviz

from langgraph.graph import StateGraph, START, END
from state import MyState
from node import increment


# StateGraph 인스턴스 생성
graph = StateGraph(MyState)

# 'increment' 노드 추가
graph.add_node("increment", increment)
# START에서 'increment' 노드로 엣지 추가
graph.add_edge(START, "increment")
# 'increment' 노드에서 END로 엣지 추가
graph.add_edge("increment", END)

# 그래프 컴파일
app = graph.compile()

# 그래프 시각화를 위한 Graphviz 객체 생성
dot = graphviz.Digraph(format='png', engine='dot')

# 노드와 엣지를 Graphviz에 추가
dot.node(START, 'START')
dot.node(END, 'END')
dot.node("increment", "increment")

dot.edge(START, "increment")
dot.edge("increment", END)

# 그래프 렌더링
dot.render("stategraph", cleanup=True)

# 그래프 파일 출력
dot.view("stategraph.png")

# 그래프 실행
result = app.invoke({"counter": 0})
print(result)  
