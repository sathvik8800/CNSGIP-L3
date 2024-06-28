def chatbot_response(user_input):
    responses = {
        "hello": "Hello buddy! How can I help you today?",
        "hi": "Hi buddy! How can I assist you?",
        "how are you": "I'm just a bot, but I'm here to help! How can I assist you?",
        "what is your name": "my name is a chatbot.",
        "help": "Sure, I'm here to help you...What do you need assistance with?",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You are welcome...! If you have any other questions, feel free to ask.",
        "thanks": "Youu are welcome....!"
    }

    user_input = user_input.lower()

    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]

    return "I'm sorry, I don't understand that. Can you please rephrase?"

def chat():
    print("Chatbot: Hello! I am your friendly chatbot. Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
