import streamlit as st
import pandas as pd

#==================================
# 제목
#==================================
st.title("스트림릿 따라하기")
st.header("Header 예제")
st.subheader("Subheader 예제")


st.text("안녕하세요")
st.write("Streamlit을 배워봅시다!")

# text와 write의 차이
# text는 순수 텍스트 출력, 
# write는 만능 출력 함수 => 거의 대부분을 출력하고 가장 많이 사용

# F12를 누르면 코드 여러 개 나오고 오른쪽 창 아래에 있는 그림을 보면 margin, border, padding, 파란 칸 해서 4칸이 그려져 있는데
# 해당 객체를 누르면 크기 및 주변 여백의 사이즈를 알 수 있음 

#==================================
# MarkDown
#==================================
st.markdown("---")
st.markdown("### Markdown")
st.markdown("## Markdown")
st.markdown("# Markdown")
st.markdown("""
- Python
- Streamlit
- LangChain
- RAG
""")

#==================================
# 코드출력
#==================================

st.markdown("---")
st.subheader("코드 출력")

code = """
for i in range(5):
    print(i)
"""
st.caption("실습중입니다.")

#==================================
# 이미지
#==================================

st.markdown("---")
st.subheader("이미지 출력")

st.image("dog.png",width=300)