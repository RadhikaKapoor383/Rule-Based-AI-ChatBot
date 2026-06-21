import random
import datetime

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "I told my computer I needed a break, and it said no problem, it'll go to sleep too.",
    "Why was the JavaScript developer sad? Because they didn't know how to null their feelings."
]

def chatbot():
    print("Chatbot: Hi! I'm a rule-based chatbot. Type 'bye' or 'exit' to quit.")
    name = None
    ended = False

    while not ended:
        user_input = input("You: ").strip().lower()

        if user_input == "":
            print("Chatbot: Please type something.")

        elif user_input.startswith(("hi", "hello", "hey")):
            print(f"Chatbot: Hello again, {name}!" if name else "Chatbot: Hello! What's your name?")

        elif user_input.startswith("my name is") or user_input.startswith("i am") or user_input.startswith("i'm"):
            name = user_input.split(maxsplit=2)[-1].strip(".!").capitalize()
            print(f"Chatbot: Nice to meet you, {name}! How can I help you today?")

        elif "how are you" in user_input:
            print(f"Chatbot: I'm doing great, thanks for asking{', ' + name if name else ''}!")

        elif "your name" in user_input or "who are you" in user_input:
            print("Chatbot: I'm a simple rule-based chatbot.")

        elif "joke" in user_input:
            print("Chatbot:", random.choice(jokes))

        elif "time" in user_input:
            print("Chatbot: The current time is", datetime.datetime.now().strftime("%H:%M:%S"))

        elif "thank" in user_input:
            print(f"Chatbot: You're welcome{', ' + name if name else ''}!")

        elif "help" in user_input:
            print("Chatbot: Try: hi, my name is ___, joke, time, thanks, or bye.")

        elif user_input.startswith(("bye", "exit", "quit")):
            print(f"Chatbot: Goodbye{', ' + name if name else ''}! Have a great day!")
            ended = True

        else:
            print("Chatbot: Sorry, I don't understand that. Try 'help'.")


if __name__ == "__main__":
    chatbot()