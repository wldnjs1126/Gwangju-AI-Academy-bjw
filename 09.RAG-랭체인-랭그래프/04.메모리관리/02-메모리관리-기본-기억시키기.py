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

# 템플릿 사용

llm = init_custom_llm()

# 대화 기록 저장소
history = [
    HumanMessage("난 홍길동이야"),
    AIMessage("네 안녕하세요. 홍길동님,무엇이든 물어보세요"),
    HumanMessage("난 홍길동이야")
]

# 프롬프트 객체 생성
prompt = ChatPromptTemplate.from_messages([
    ("system","당신은 친절한 비서 입니다."),
    ## history라는 이름으로 전달되는 대화 내용을 여기에 넣어라
    MessagesPlaceholder("history")
])
#  MessagesPlaceholder => 기억 유지하는 함수

while True:
    question = input("질문 : ")

    history.append(
        HumanMessage(question)
    )

    chain = prompt | llm

    response = chain.invoke({
        "history" : history
    })

    history.append(AIMessage(response.content))
    print("AI 응답",response.content)

    # 2. 비용 증가
    # 긴 대화는 더 많은 토큰을 사용합니다. API 비용이 증가합니다.

    # 대화가 너무 길면 LLM이 중요한 정보를 놓칠 수 있습니다.
    # 속도 저화 