from rag import ask

print("=" * 50)
print("전주 맛집 가이드")
print("=" * 50)

while True:
    question = input("질문 : ")

    if question == "exit":
        break

    answer = ask(question)
    print()
    print(answer)