import streamlit as st
import pandas as pd

# 사용자 입력 받기
# Widget 값 저장
# 입력 결과 출력

# st.title("스트림릿 입력 위젯")

st.markdown(
    "<h1>스트림릿 <span style='color:#FFD700;'>입력</span> 위젯</h1>",
    unsafe_allow_html=True
)

# 텍스트 입력
name = st.text_input("이름 입력")

st.markdown("---")

# 숫자 입력
age = st.number_input(
    "나이",
    min_value=0,
    max_value=100,
    value=20
)

st.markdown("---")

# 선택 박스
job = st.selectbox(
    "직업 선택",
    [
        "학생",
        "개발자",
        "회사원",
        "디자이너"
    ]
)

st.markdown("---")

# 멀티 셀렉트
hobby = st.multiselect(
    "취미 선택",
    [
        "운동",
        "독서",
        "게임",
        "여행"
    ]
)

st.markdown("---")

gender = st.radio(
    "성별",
    [
        "남자",
        "여자"
    ]
)

st.markdown("---")

agress = st.checkbox("개인 정보 수집 동의")

st.markdown("---")

# 슬라이더
score = st.slider(
    "점수",
    0,
    100,
    50
)

st.markdown("---")

# 날짜와 시간
st.divider()
date = st.date_input("생년월일")

st.divider()
time = st.time_input("출근 시간")

st.write("이름 : ", name)
st.write("나이 : ", age)
st.write("직업 : ", job)
st.write("취미 : ", hobby)
st.write("성별 : ", gender)
st.write("동의 : ", agress)
st.write("점수 : ", score)
st.write("날씨 : ", date)
st.write("시간 : ", time)

# <div>My first paragraph.</div>
# <div>My first paragraph.</div> 이라 작성하면 두 줄로 나뉘어 나오는데 
# div 에서 span 으로 바꿔 입력하면 My first paragraph. My first paragraph. 이렇게 가로로 붙혀서 출력됨 
