from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    score:int
    result:str

# node
def check(state):
    print("|n 점수검사",state["score"])
    return state

def pass_node(state):
    state["result"]="합격"
    return state

def fail_node(state):
    state["result"]="불합격"
    return state

# 조건함수 = 분기
def route(state):

    if state["score"] >= 60:
        return "pass"
    
    return "fail"

# Graph 객체 생성
builder = StateGraph(State)

builder.add_node("check",check)
builder.add_node("pass",pass_node)
builder.add_node("fail",fail_node)

builder.add_edge(START,"check")
builder.add_conditional_edges(
    "check",
    route,
    {
        "pass":"pass",
        "fail":"fail"
    }
)

builder.add_edge("pass",END)
builder.add_edge("fail",END)

graph = builder.compile()

# 실행

result = graph.invoke({
    "score":80
})

print(result)
print(result["result"])

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))


from util import show_graph
show_graph(graph)

# ============================================================

class State(TypedDict):
    age: int
    result: str

# 성인 여부 판별
# 그래프

# START
#   ↓
# check_age
#   ↓
#    ├── adult
#    └── child
#        ↓
#       END
# 초기값
# age = 20
# 결과
# 성인

# 조건
# 19세 이상 → adult
# 19세 미만 → child

# node
def check_age(state):
    print("|n 나이확인",state["age"])
    return state

def adult_node(state):
    state["result"]="adult"
    return state

def child_node(state):
    state["result"]="child"
    return state

# 조건함수 = 분기
def route(state):

    if state["age"] >= 19:
        return "adult"
    
    return "child"

# Graph 객체 생성
builder = StateGraph(State)

builder.add_node("check",check_age)
builder.add_node("adult",adult_node)
builder.add_node("child",child_node)

builder.add_edge(START,"check")
builder.add_conditional_edges(
    "check",
    route,
    {
        "adult":"adult",
        "child":"child"
    }
)

builder.add_edge("adult",END)
builder.add_edge("child",END)

graph = builder.compile()

# 실행

result = graph.invoke({
    "age":20
})

print(result)
print(result["result"])

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))


from util import show_graph
show_graph(graph)
