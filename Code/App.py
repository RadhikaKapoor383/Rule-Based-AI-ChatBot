import random
import re
import datetime

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "I told my computer I needed a break, and it said no problem, it'll go to sleep too.",
    "Why was the JavaScript developer sad? Because they didn't know how to null their feelings."
]

facts = [
    "Honey never spoils if stored properly.",
    "Octopuses have three hearts.",
    "A bolt of lightning is hotter than the surface of the sun.",
    "Bananas are berries, but strawberries aren't."
]

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal. - Winston Churchill",
    "Simplicity is the soul of efficiency. - Austin Freeman"
]

compliments = [
    "You're doing great, keep going!",
    "Your curiosity is impressive.",
    "You ask really good questions."
]

random_talks = [
    "Did you know the chatbot you're talking to runs entirely on if-else logic?",
    "Here's a thought: the best time to plant a tree was yesterday, the next best time is today.",
    "Fun fact: this conversation exists because of a single while loop.",
    "I don't have much to say, but I do enjoy a good joke. Want to hear one?",
    "Life tip: take a short break, stretch, and drink some water.",
]

negative_words = ["sad", "angry", "upset", "tired", "stressed", "bad", "depressed", "frustrated"]
positive_words = ["happy", "great", "excited", "good", "awesome", "fantastic"]


def calculate(expression):
    """Safely evaluate a basic arithmetic expression like '5 + 3' or '12 * 4'."""
    cleaned = re.sub(r"[^0-9+\-*/().\s]", "", expression)
    if not cleaned.strip():
        return None
    try:
        result = eval(cleaned, {"__builtins__": {}})
        return result
    except Exception:
        return None


def get_response(user_input, name=None, ended=False):
    """
    Core rule-based logic.
    Takes the raw user input plus current state (name, ended),
    returns (reply_text, updated_name, updated_ended).
    """
    raw = user_input.strip()
    user_input = raw.lower()

    if ended:
        return "Chatbot: The conversation has ended. Restart to chat again.", name, ended

    if user_input == "":
        return "Chatbot: Please type something.", name, ended

    # --- Sentiment-aware check (runs before generic matching) ---
    if any(word in user_input for word in negative_words):
        reply = "Chatbot: I'm sorry to hear that. I hope things get better soon."
        return reply, name, ended

    if any(word in user_input for word in positive_words):
        reply = "Chatbot: That's wonderful to hear!"
        return reply, name, ended

    # --- Calculator: detect expressions like "5 + 3" or "calculate 12*4" ---
    calc_match = re.search(r"(-?\d+(\.\d+)?\s*[\+\-\*/]\s*-?\d+(\.\d+)?(\s*[\+\-\*/]\s*-?\d+(\.\d+)?)*)", user_input)
    if "calculate" in user_input or calc_match:
        expr = calc_match.group(1) if calc_match else user_input.replace("calculate", "")
        result = calculate(expr)
        if result is not None:
            return f"Chatbot: {expr.strip()} = {result}", name, ended
        return "Chatbot: I couldn't compute that. Try something like '5 + 3'.", name, ended

    # --- Date / day lookup ---
    if "what day is it" in user_input or "today's date" in user_input or "what is the date" in user_input:
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        return f"Chatbot: Today is {today}.", name, ended

    if user_input.startswith(("hi", "hello", "hey")):
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

    elif "fact" in user_input:
        return f"Chatbot: Did you know? {random.choice(facts)}", name, ended

    elif "quote" in user_input:
        return f"Chatbot: {random.choice(quotes)}", name, ended

    elif "compliment" in user_input:
        return f"Chatbot: {random.choice(compliments)}", name, ended

    elif "time" in user_input:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Chatbot: The current time is {now}", name, ended

    elif "thank" in user_input:
        reply = f"Chatbot: You're welcome{', ' + name if name else ''}!"
        return reply, name, ended

    elif "tell me something" in user_input or "tell me anything" in user_input or "say something" in user_input:
        return f"Chatbot: {random.choice(random_talks)}", name, ended

    elif "help" in user_input:
        return (
            "Chatbot: Try: hi, my name is ___, joke, fact, quote, compliment, "
            "time, what day is it, calculate 5 + 3, tell me something, thanks, or bye.",
            name,
            ended,
        )

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