from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI

load_dotenv()

# LLM 객체 생성 방법 3가지 (Large Language Model)

# # 첫번째 방법 : OpenAI()로 객체 생성 (간단하게 invoke 함수를 사용해서 할 수 있음, str 형태로 답변을 줌)
# llm = OpenAI()
# result = llm.invoke("대한민국 수도는?")
# print(type(result))
# print(result)

# # 두번째 방법 : OpenAI()로 객체 생성 (간단하게 보면 챗지피티를 가지고 오는 것)
# llm = ChatOpenAI()
# result = llm.invoke("대한민국 수도는?")
# print(result.content)
# print(result)

# # 세번째 방법
# from langchain.chat_models import init_chat_model
# import os

# model_name = os.getenv("LLM_AI_MODEL")
# llm = init_chat_model(model_name)

# respose = llm.invoke("오늘 날씨 어때?")
# print(respose.content)
# print(respose)

import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
#print(os.listdir(Path(__file__).resolve().parent.parent))

from llm_loader import init_custom_llm

print(init_custom_llm)

llm = init_custom_llm()
respose = llm.invoke("오늘 날씨 어때?")

print(respose.content)
print(respose)