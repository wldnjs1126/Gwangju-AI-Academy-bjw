from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm

# 템플릿 사용

llm = init_custom_llm()

# 첫 번째 질문
response = llm.invoke("안녕하세요. 제 이름은 홍길동입니다.")
print("응답",response.content)
# 응답 안녕하세요, 홍길동님! 만나서 반갑습니다. 어떻게 도와드릴까요?

# 두 번째 질문
response = llm.invoke("제 이름은 뭐 였죠?")
print("응답2",response.content)
# 응답2 죄송하지만, 당신의 이름을 알 수 있는 정보가 없습니다. 당신의 이름을 알려주시면 그에 맞춰 대화할 수 있습니다!