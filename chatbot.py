# ChattyBot - A Simple Python Chatbot

print("🤖 Hello! I'm ChattyBot.")
name = input("What's your name? ")
print(f"Nice to meet you, {name}! Type 'bye' to exit.")

while True:
    message = input(f"{name}: ").lower()

    if "bye" in message:
        print("🤖 Goodbye! Talk to you later. 👋")
        break
    elif "how are you" in message:
        print("🤖 I'm just a bot, but I'm doing great! How about you?")
    elif "weather" in message:
        print("🤖 I hope it's sunny where you are! ☀️")
    elif "joke" in message:
        print("🤖 Why did the computer go to therapy? Because it had too many bytes! 😂")
    elif "sad" in message or "tired" in message:
        print("🤖 I'm sending you a virtual hug 💖. You'll be okay.")
    else:
        print("🤖 Hmm... I don't know how to respond to that yet.")
