from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
import sys
from pathlib import Path
import os
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage


sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm

#============================================================
# 예제 1. 리스트로 대화 저장하기 (Memory가 없을 때)
history = []

history.append("사용자 : 안녕하세요.")
history.append("AI : 안녕하세요!")

history.append("사용자 : 제 이름은 철수입니다.")
history.append("AI : 반갑습니다 철수님.")

print(history)

# 문자열만 저장하면 AI가 이해할 수 있을까요?"
# AI는 누가 말했는지(Human/AI)를 알아야 함

from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage

history = []

history.append(HumanMessage("안녕하세요."))
history.append(AIMessage("안녕하세요!"))

history.append(HumanMessage("제 이름은 철수입니다."))
history.append(AIMessage("반갑습니다 철수님."))

print(history)

# ChatMessageHistory 등장
from langchain_community.chat_message_histories import ChatMessageHistory

history = ChatMessageHistory()  # 메모리 관리하는 함수 ChatMessageHistory, InMemoryChatMessageHistory, RunnableWithMessageHistory
history.add_user_message("안녕하세요")
history.add_ai_message("무엇을 도와드릴까요?")

print(history.messages)

for message in history.messages:
    print(type(message))
    print(message.content)

# [
#     HumanMessage(content="안녕하세요",additinal_kwargs={},response_metadata={}),
#     AIMessage(content="무엇을 도와드릴까요?",additinal_kwargs={},response_metadata={}, tool_calls={}, invalid_tool_calls=[])
# ]

# 템플릿 사용

llm = init_custom_llm()

