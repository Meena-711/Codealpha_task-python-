import datetime

def chatbot_reply(message):
    message = message.lower()

    # --- Basic Greetings ---
    if "hello" in message or "hi" in message:
        return "Hello! 👋 How can I assist you today?"
    
    if "how are you" in message:
        return "I'm doing great! 😊 Thanks for asking."

    # --- Jokes ---
    if "joke" in message:
        jokes = [
            "Why don’t programmers like nature? It has too many bugs! 🐞😂",
            "Why was the computer cold? It forgot to close its Windows! 🪟🤣",
            "What do you call a robot that takes a long route? R2-Detour! 🤖😆"
        ]
        import random
        return random.choice(jokes)

    # --- Weather (Simple Predefined Text) ---
    if "weather" in message:
        return "I can't check live weather ⛈ but usually it's either sunny, rainy, or perfect for coding 😎."

    # --- Date ---
    if "date" in message:
        today = datetime.date.today()
        return f"Today's date is {today.strftime('%d-%m-%Y')} 📅"

    # --- Time ---
    if "time" in message:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now} ⏰"

    # --- Thank you ---
    if "thank" in message:
        return "You're welcome! 😊 Happy to help."

    # --- About chatbot ---
    if "your name" in message:
        return "I'm your friendly Python Chatbot 🤖!"

    if "what can you do" in message:
        return "I can chat, tell jokes, give date/time, and make your coding journey fun! 😄"

    # --- Exit ---
    if "bye" in message or "exit" in message:
        return "Goodbye! 👋 Have a great day!"

    # --- Default ---
    return "I'm not sure I understand 🤔 Could you try saying something else?"


print("Chatbot: Welcome! Type 'bye' to exit.\n")

while True:
    user = input("You: ")
    reply = chatbot_reply(user)
    print("Chatbot:", reply)

    if "bye" in user.lower() or "exit" in user.lower():
        break
