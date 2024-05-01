import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["꽤나 흥미롭네요. 더 말씀해주시겠어요?",
                    "이해했습니다. 계속 말씀해주세요.",
                    "왜 그렇게 말씀하셨나요?",
                    "날씨가 재밌네요. 그렇지 않나요?",
                    "주제를 바꾸어봅시다.",
                    "어젯밤 경기 보셨나요?"]

print("안녕하세요. 저는 간단한 로봇, Marvin입니다.")
print("'bye'를 입력하면 언제든지 이 대화를 끝낼 수 있습니다.")
print("대답한 이후에는 'enter'를 입력하세요.")
print("오늘 기분은 어떠신가요?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input.lower() == "bye":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("It was nice talking to you, goodbye!")
