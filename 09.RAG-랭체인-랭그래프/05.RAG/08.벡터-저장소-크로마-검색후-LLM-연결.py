# pip install langchain-community faiss-cpu
# pip install chromadb langchain-chroma langchain-huggingface

# | Vector Store  | 메모리 저장 | 디스크 저장 | 서버 필요 | 실무 사용 |
# | ------------- | ------ | ------ | ----- | ----- |
# | FAISS         | ✅      | ✅      | ❌     | ⭐⭐⭐⭐⭐ |
# | Chroma        | ✅      | ✅      | ❌     | ⭐⭐⭐⭐⭐ |
# | Milvus        | ✅      | ✅      | ✅     | ⭐⭐⭐⭐⭐ |
# | Qdrant        | ✅      | ✅      | ✅     | ⭐⭐⭐⭐⭐ |
# | Pinecone      | 클라우드   | 클라우드   | 관리형   | ⭐⭐⭐⭐⭐ |
# | Weaviate      | ✅      | ✅      | ✅     | ⭐⭐⭐⭐  |
# | Redis         | ✅      | 일부     | ✅     | ⭐⭐⭐⭐  |
# | Elasticsearch | ✅      | ✅      | ✅     | ⭐⭐⭐⭐  |

# =========================================================================

from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path
from langchain_chroma import Chroma

embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
)

BASE_DIR = Path(__file__).resolve().parent #현재 실행 중인 파이썬 파일이 있는 폴더의 절대 경로를

documents = [
    "고양이는 귀여운 동물입니다.",
    "강아지는 충성심이 강합니다.",
    "자동차는 빠르게 달립니다."
]

# Chroma DB 저장 폴더
DB_PATH = BASE_DIR / "chroma_db"

db = Chroma.from_texts(
    texts=documents,
    embedding=embedding,
    persist_directory=str(DB_PATH)
)

print("벡터 DB 생성")

# Retriever 생성
retriever = db.as_retriever(
    # search_kwargs={"k":3}
)

# 검색하기 
question = "고양이는 어떤 동물인가요?"
docs = retriever.invoke(question) 
# retriever 객체에 자연어를 집어넣으면 유사도를 따져서 해당 벡터 공간에 있는 4개의 답변을 출력 (기본적으로 4개 출력)

print(type(docs))

for doc in docs:
    print("="*50)
    print(doc.page_content)

# ==================================================
# 고양이는 귀여운 동물입니다.
# ==================================================
# 고양이는 귀여운 동물입니다.
# ==================================================
# 고양이는 귀여운 동물입니다.
# ==================================================
# 강아지는 충성심이 강합니다.

# LLM 연결

import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm
# 템플릿 사용
from langchain_core.prompts import PromptTemplate

llm = init_custom_llm()

context = ""

for doc in docs:
    context = context + doc.page_content
    context = context + "|n"

prompt = f"""
당신은 친절한 AI입니다.

아래의 문서를 참고하여 답변하세요.

문서:
{context}

질문:
{question}
"""

response = llm.invoke(prompt)

print("=" * 50)
print(response.content)