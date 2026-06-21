import random
import datetime

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "I told my computer I needed a break, and it said no problem, it'll go to sleep too.",
    "Why was the JavaScript developer sad? Because they didn't know how to null their feelings."
]


def get_response(user_input, name=None, ended=False):
    """
    Core rule-based logic.
    Takes the raw user input plus current state (name, ended),
    returns (reply_text, updated_name, updated_ended).
    """
    user_input = user_input.strip().lower()

    if ended:
        return "Chatbot: The conversation has ended. Restart to chat again.", name, ended

    if user_input == "":
        return "Chatbot: Please type something.", name, ended

    elif user_input.startswith(("hi", "hello", "hey")):
        reply = f"Chatbot: Hello again, {name}!" if name else "Chatbot: Hello! What's your name?"
        return reply, name, ended

    elif user_input.startswith("my name is") or user_input.startswith("i am") or user_input.startswith("i'm"):
        new_name = user_input.split(maxsplit=2)[-1].strip(".!").capitalize()
        reply = f"Chatbot: Nice to meet you, {new_name}! How can I help you today?"
        return reply, new_name, ended

    elif "how are you" in user_input:
        reply = f"Chatbot: I'm doing great, thanks for asking{', ' + name if name else ''}!"
        return reply, name, ended

    elif "your name" in user_input or "who are you" in user_input:
        return "Chatbot: I'm a simple rule-based chatbot.", name, ended

    elif "joke" in user_input:
        return f"Chatbot: {random.choice(jokes)}", name, ended

    elif "time" in user_input:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Chatbot: The current time is {now}", name, ended

    elif "thank" in user_input:
        reply = f"Chatbot: You're welcome{', ' + name if name else ''}!"
        return reply, name, ended

    elif "help" in user_input:
        return "Chatbot: Try: hi, my name is ___, joke, time, thanks, or bye.", name, ended

    elif user_input.startswith(("bye", "exit", "quit")):
        reply = f"Chatbot: Goodbye{', ' + name if name else ''}! Have a great day!"
        return reply, name, True

    else:
        return "Chatbot: Sorry, I don't understand that. Try 'help'.", name, ended


def chatbot():
    """Console version — runs in a continuous loop until the user exits."""
    print("Chatbot: Hi! I'm a rule-based chatbot. Type 'bye' or 'exit' to quit.")
    name = None
    ended = False

    while not ended:
        user_input = input("You: ")
        reply, name, ended = get_response(user_input, name, ended)
        print(reply)


if __name__ == "__main__":
    chatbot()