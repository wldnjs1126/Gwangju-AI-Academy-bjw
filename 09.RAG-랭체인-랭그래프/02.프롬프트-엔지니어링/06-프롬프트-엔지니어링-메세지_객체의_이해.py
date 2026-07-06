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

# 메세지란?



llm = init_custom_llm()
respose = llm.invoke(result)

print(respose.content)
