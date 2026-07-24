import streamlit as st

st.title("다운로드 업로드 버튼")

if st.button("클릭"):
    st.success("버튼 클릭!")

text = "스트림릿 다운로드 테스트"

st.download_button(
    label="파일 다운로드",
    data=text,
    file_name="text.txt"
)

