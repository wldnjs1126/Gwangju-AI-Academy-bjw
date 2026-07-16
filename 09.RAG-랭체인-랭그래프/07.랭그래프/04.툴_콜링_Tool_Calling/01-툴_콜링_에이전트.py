from dotenv import load_dotenv
from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    START,
    END
)

import os

# ==========================
# 환경변수
# ==========================

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from llm_loader import init_custom_llm

llm = init_custom_llm()

from langchain_core.tools import tool
from  datetime import datetime

@tool
def age(birth_year):
    """
    출생연도를 입력받아 현재 나이를 계산합니다.
    """
    
    current_year = datetime.now().year
    
    return current_year - birth_year