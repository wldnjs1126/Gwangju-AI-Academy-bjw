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
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser, XMLOutputParser

from pydantic import BaseModel

class UseInfo(BaseModel):
    name : str
    age : int
    job : str

llm = init_custom_llm()
structured_llm = llm.with_structured_output(UseInfo)
# structured_llm을 사용하면 클래스를 사용하여 구조화된 출력물이 나옴 


result = structured_llm.invoke("김철수 25살 개발자야")

print(result)
print("성명 :",result.name)
print("나이 :",result.age)
print("직업 :",result.job)

print(result.model_dump())
# {'name': '김철수', 'age': 25, 'job': '개발자'} 와 같이 Json 형식으로 출력# 첫번째 질문
