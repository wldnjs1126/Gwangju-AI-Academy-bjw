from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from openai import OpenAI

import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage
# 잘 모르겠으면 모든걸 가져오겠다는 뜻의 " * " 을 사용해도 됨 

# 메세지란?
# System
# 당신은 친절한 AI입니다.

# Human
# AI 란 무엇인가요?

# AI
# AI는 인공지능입니다.

# Human
# 예제를 보여주세요

# 한 줄의 대화 = message 객체 하나로 관리
# 결론) 전체 대화 = Message List

# 1. 시스템 메세지 만들기
system = SystemMessage(content="당신은 친절한 분석가입니다.")
print(system)
print(system.content)

# 2. AI 메세지 만들기
ai = AIMessage(
    content="AI는 사람처럼 학습하는 기술입니다."
)

print(ai.content)

# 3. 유저 질문
human = HumanMessage(content="클래스에 대해 설명해줘")
print(human.content)

# 4. Tool 함수
tool = ToolMessage(
    content = "5",
    tool_call_id = "call_1234"
)

messages = [
    system,
    ai,
    human
]

llm = init_custom_llm()
respose = llm.invoke(messages)

print(respose.content)

# invoke 뒤에 사용이 가능한 객체들은 f - string을 사용하거나 prompttemplate을 사용해서 
# result = prompt.invoke({"topic" : "머신러닝"})와 같이 사용하거나
# Chatprompttemplate을 사용해서 result = messages.invoke({"topic","딕셔너리"}) 와 같은 방식으로 사용함 
# 물론 respose = llm.invoke(messages)와 같이 변수에 대입시킨 후 집어 넣을 수도 있음 
