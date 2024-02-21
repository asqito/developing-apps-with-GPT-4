import openai

# 여기서 "your_openai_api_key"를 실제 OpenAI API 키로 교체
OPENAI_API_KEY = "your_openai_api_key"

# OpenAI API 키를 전역 환경변수로 설정
openai.api_key = OPENAI_API_KEY

# 대화 시작
def start_chat():
    messages = []

    # 대화 종료 조건에 대한 안내
    print("AI와 대화를 시작합니다. 대화를 종료하려면 'exit'를 입력하세요.")

    while True:
        user_input = input("You: ")
        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
        # openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # ai_response = response.choices[0].message['content'] <= 오류 발생 
        ai_response = response.choices[0].message.content
        print(f"AI: {ai_response}")
        
        # 사용자 입력과 AI 응답을 저장
        messages.append({"role": "assistant", "content": ai_response})

        # 현재 대화 상태 확인 (선택적)
        # print("Current conversation state:")
        # for msg in messages:
        #    print(f"{msg['role']}: {msg['content']}")
        
        # 대화 종료 조건 (예시: 사용자가 'exit' 입력)
        if user_input.lower() == 'exit':
            break

# 대화 시작 함수 호출
start_chat()
