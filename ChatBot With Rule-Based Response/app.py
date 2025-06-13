import re
import random

def get_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if re.search(r'\b(hi|hello|hey|hola)\b', user_input):
        return "Hello! How can I help you today?"

    # Asking about chatbot
    elif re.search(r'\b(who|what) are you\b', user_input):
        return "I'm a simple chatbot created to respond to your questions."

    # Asking for help
    elif "help" in user_input:
        return "Sure! I can help you with general questions. Ask me anything."

    # Asking about time
    elif "time" in user_input:
        from datetime import datetime
        return "Current time is: " + datetime.now().strftime("%H:%M:%S")

    # Asking about date
    elif "date" in user_input:
        from datetime import datetime
        return "Today's date is: " + datetime.now().strftime("%d-%m-%Y")

    # Asking how the bot is
    elif re.search(r'\bhow are you\b', user_input):
        return "I'm just code, but thanks for asking! How are you?"

    # Asking bot’s name
    elif re.search(r'\bwhat(?:\'s| is |s) your name\b', user_input):
        return "You can call me ChatPy!"

    # Asking for a joke
    elif "joke" in user_input:
        jokes = [
            "Why don't programmers like nature? It has too many bugs.",
            "Why did the computer get cold? Because it forgot to close its Windows!",
            "I would tell you a UDP joke, but you might not get it.",
            "Why do Java developers wear glasses? Because they don’t see sharp."
        ]
        return random.choice(jokes)

    # Asking for weather (dummy reply)
    elif "weather" in user_input:
        return "I'm not connected to the internet, but it looks like a great day to code!"

    # Simple math (basic + - * /)
    elif re.search(r'(\d+)\s*([+\-*/])\s*(\d+)', user_input):
        match = re.search(r'(\d+)\s*([+\-*/])\s*(\d+)', user_input)
        num1, op, num2 = match.groups()
        num1, num2 = int(num1), int(num2)
        result = {
            '+': num1 + num2,
            '-': num1 - num2,
            '*': num1 * num2,
            '/': round(num1 / num2, 2) if num2 != 0 else "undefined (division by zero)"
        }[op]
        return f"The answer is: {result}"


    # Goodbye
    elif re.search(r'\b(bye|exit|quit)\b', user_input):
        return "Goodbye! Have a great day."

    # Default response
    else:
        return "I'm not sure how to respond to that. Can you rephrase?"

def chat():
    print("🤖 Chatbot: Hi there! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("🤖 Chatbot: Goodbye! Have a great day")
            break
        response = get_response(user_input)
        print("🤖 Chatbot:", response)

if __name__ == "__main__":
    chat()
