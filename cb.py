import random

successful_interactions = 0

user_needs=["get info","ask question","request assistance"]

chatbot_personality={
    "greeting":["hello","hi","hey","how are you"],
    "farewell":["bye","goodbye","see you"],
    "positive":["great","awesome","good","fantastic"],
    "negative":["sorry","apologies"],
    "unknown":["i am only trained in some aspects","sorry i dont know i am only basic design"]
}

chatbot_flow ={
     "greeting":["hello","hi","hey","how are you"],
    "farewell":["bye","goodbye","see you"],
    "positive":["great","awesome","good","fantastic"],
    "negative":["sorry","apologies"],
    "unknown":["i am not sure","i cant answer that"],
    "info":["sorry i am only trained for limited responses "],
    "goats":["i would choose messi","i prefer messi"],
    "strengths":["i am a chatbot designed to help you in some aspects"]

}

def get_user_input():
    user_input=input("user:")
    return user_input.lower()

def generate_chatbot_response(user_input):
    chatbot_response=""
    user_input=user_input.lower()

    if any (need in user_input for need in user_needs):
        chatbot_response=random.choice(chatbot_flow["info"])
        global successful_interactions
        successful_interactions += 1
    elif "hi" in user_input or "hello" in user_input:
        chatbot_response=random.choice(chatbot_flow["greeting"])
    elif "how are you" in user_input or "how you doing" in user_input:
        chatbot_response=random.choice(chatbot_flow["positive"]) 
    elif "bye" in user_input or "goodbye" in user_input:
        chatbot_response=random.choice(chatbot_flow["farewell"]) 
    elif "what can you do" in user_input or "what are your capabilities" in user_input:
        chatbot_response=random.choice(chatbot_flow["strengths"])
    elif "who is goat" in user_input or "messi or ronaldo" in user_input:
        chatbot_response=random.choice(chatbot_flow["goats"])
    else:
        chatbot_response=random.choice(chatbot_flow["info"])
    return chatbot_response

def start_chatbot():
    while True:
        user_input=get_user_input()
        if user_input=="exit":
            break
        chatbot_response=generate_chatbot_response(user_input)
        print("chatbot:"+ chatbot_response)

print("welcome to chatbot")


print("chatbot:"+"how may i assist you today")
start_chatbot()

print("successful interaction:"+str(successful_interactions))

