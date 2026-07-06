from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate


import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm
# 템플릿 사용
from langchain_core.prompts import PromptTemplate

llm = init_custom_llm()

topics=[
    "Python",
    "Django",
    "React"
]

prompt = PromptTemplate.from_template("""
당신은 파이썬 강사입니다.
주제 : 반복문
초보라도 이해할 수 있게 설명하세요.                                      
""")

# for t in topics:
#     formatted = prompt.format(topic = t)
#     respose = llm.invoke(formatted)
#     print("==========")
#     print(respose.content)

# 체인 연결
# 1. chain
# 여러 자격을 순서대로 연결 

chain = prompt| llm  # | <= 체인을 의미함

result = chain.invoke({
    "topic" : "반복문"
})

print(result.content)

# 체인으로 연결할 수 있는 객체 : 프롬프트, LLM, 출력 파서 (LLM의 자유로운 텍스트 → 프로그램에서 사용하기 쉬운 형태로 바꿔주는 단계)

# langchain이 필요한 이유
# - 복잡한 LLM 애플리케이션을 빠르게 개발 가능
# - 다양한 모델과 데이터 소스를 손쉽게 연결할 수 있음

