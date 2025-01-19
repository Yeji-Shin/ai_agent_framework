from dotenv import load_dotenv
from graph import app

load_dotenv()

def run_graph(query):
    result = app.invoke({"query": query})
    return result

if __name__ == "__main__":
    app.get_graph().draw_mermaid_png(output_file_path="./graph.png")
    user_query = "오늘 영국 날씨 어때요?"
    result = run_graph(user_query)
    print(result)