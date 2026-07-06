# 프롬프트 = AI에게 무엇을 어떻게 해달라고 지시하는 입력

# 프롬프트(Pronpt)는 생성형  AI가 원하는 결과를 만들어낼 수 있도록
# 역할(role), 목적(Task), 맥락(Context), 제약 조건(Constraints), 출력 형식(Output Format) 등을 전달하는 자연어 기반의 지시서(Instruction)
# AI가 문제를 이해하고, 추론하며, 원하는 형태의 결과를 생성하도록 안내하는 설계도


# 페르소나 => (인물설정)
# AI의 성격 + 경력 + 말투를 지정


from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from openai import OpenAI

# 제로샷 :  예시가 없음 => 모델이 바로 답변 (AI가 기준없이 바로 답변 생성)

prompt = """
다음 문장을 영어로 번역하세요.

나는 오늘 학교에 갔다.
"""
import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent)) 
from llm_loader import init_custom_llm

print(init_custom_llm)

llm = init_custom_llm()
respose = llm.invoke(prompt)

print(respose.content)

