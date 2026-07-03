from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI

load_dotenv()

# LLM 객체 생성 방법 3가지 (Large Language Model)

# 첫번째 방법 : OpenAI()로 객체 생성 (간단하게 invoke 함수를 사용해서 할 수 있음, str 형태로 답변을 줌)
# llm = OpenAI()
# result = llm.invoke("대한민국 수도는?")
# print(type(result))
# print(result)

# 두번째 방법 : OpenAI()로 객체 생성 (간단하게 보면 챗지피티를 가지고 오는 것)
llm = ChatOpenAI()
result = llm.invoke("대한민국 수도는?")
print(result.content)
print(result)