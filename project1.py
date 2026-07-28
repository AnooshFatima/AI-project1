def get_response(message):
    text = message.strip().lower()

    greetings = {"hi", "hello", "hey", "good morning", "good evening"}
    exits = {"bye", "exit", "quit"}

    if text in greetings:
        return "Hello! I'm your rule-based AI assistant. How can I help you today?"

    elif text in exits:
        return "Goodbye! Have a wonderful day.", True

    elif "name" in text:
        return "I am DecodeBot, a rule-based AI chatbot created for Internship Project 1."

    elif "ai" in text:
        return "Artificial Intelligence is the field of creating systems that can perform tasks requiring human intelligence."

    elif "thank" in text:
        return "You're welcome! Happy to help."

    else:
        return "I'm still learning through rules. Please try greetings, ask my name, or ask about AI."

    return None


print("=== DecodeBot ===")
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ")

    result = get_response(user)

    if isinstance(result, tuple):
        reply, should_exit = result
        print("Bot:", reply)
        if should_exit:
            break
    else:
        print("Bot:", result)