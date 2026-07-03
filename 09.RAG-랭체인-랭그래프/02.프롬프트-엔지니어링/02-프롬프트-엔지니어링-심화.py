# 프롬프트 = AI에게 무엇을 어떻게 해달라고 지시하는 입력

# 프롬프트(Pronpt)는 생성형  AI가 원하는 결과를 만들어낼 수 있도록
# 역할(role), 목적(Task), 맥락(Context), 제약 조건(Constraints), 출력 형식(Output Format) 등을 전달하는 자연어 기반의 지시서(Instruction)
# AI가 문제를 이해하고, 추론하며, 원하는 형태의 결과를 생성하도록 안내하는 설계도


# 1. 페르소나
# AI의 성격 + 경력 + 말투를 지정

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from openai import OpenAI

load_dotenv()

from openai import OpenAI

client = OpenAI()


prompt = """
당신은 다음 특징을 가진 AI입니다.

[Persona]
- 10년차 데이터 사이언티스트
- 삼성전자 AI 연구원 출신
- 친절하고 쉽게 설명하는 스타일

[Task]
머신러닝이 무엇인지 설명하세요.

[Constraint]
- 5줄 이내
- 비유 1개 포함
- 초보자 대상
"""

response = client.responses.create(
    model="gpt-4o-mini",
    input=prompt
)

print(response.output_text)

import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent)) # 첫번째 부모 : 02.프롬프트-엔지니어링 폴더, 두번째 부모 : 09.RAG-랭체인 폴더
from llm_loader import init_custom_llm

print(init_custom_llm)

llm = init_custom_llm()
respose = llm.invoke(prompt)

print(respose.content)
# print(respose)
