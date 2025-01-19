from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# .env 파일에서 환경 변수 로드
load_dotenv()

# GPT-4o-mini 설정
gpt4o_mini = ChatOpenAI(
    model_name="gpt-4o-mini",  # GPT-4o-mini에 해당하는 모델명
    temperature=0.7,
    max_tokens=150,
)

# GPT-4o 설정
gpt4o = ChatOpenAI(
    model_name="gpt-4o",  # GPT-4o에 해당하는 모델명
    temperature=0.7,
    max_tokens=300,
)

# GPT-4o-mini 사용
response_mini = gpt4o_mini.invoke([HumanMessage(content="Hello, how are you?")])
print(response_mini.content)

# GPT-4o 사용
response_full = gpt4o.invoke([HumanMessage(content="Explain the concept of machine learning.")])
print(response_full.content)
