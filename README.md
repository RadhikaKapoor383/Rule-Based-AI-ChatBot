# Rule-Based AI Chatbot

A simple rule-based chatbot that responds to predefined user inputs using if-else control flow. It is available in two forms: a command-line console version and a Streamlit-based graphical interface.

## Features

- Greeting recognition (`hi`, `hello`, `hey`)
- Name capture and personalized responses
- Small talk: how are you, jokes, facts, quotes, compliments
- Sentiment-aware replies based on detected mood keywords
- Basic calculator for simple arithmetic expressions
- Current time and date lookup
- Open-ended small talk via "tell me something"
- Graceful exit handling (`bye`, `exit`, `quit`) with a conversation summary
- Continuous loop until an exit command is received

## Project Structure

```
Rule-based-AI-chatbot/
├── Code/
│   └── App.py            # Core chatbot logic (shared by console and GUI)
├── Gui/
│   ├── chatbot-gui.py     # Streamlit graphical interface
│   └── .streamlit/
│       └── config.toml   # Theme configuration
├── .gitignore
└── README.md
```

## Requirements

- Python 3.8 or later
- Streamlit (for the GUI version only)

Install dependencies:

```bash
pip install streamlit
```

## Usage

### Console version

Run the chatbot directly in a terminal:

```bash
cd Code
python App.py
```

Type messages at the `You:` prompt. Type `bye`, `exit`, or `quit` to end the session.

### Streamlit GUI version

Run the graphical interface:

```bash
cd Gui
streamlit run chatbot-gui.py
```

This opens the chatbot in your default web browser at `http://localhost:8501`.

## How It Works

The chatbot's decision-making logic lives in a single function, `get_response()`, defined in `Code/App.py`. This function:

1. Accepts the current user input along with conversation state (the user's name and whether the conversation has ended)
2. Matches the input against a sequence of if-else conditions, each representing a recognized intent
3. Returns a response along with any updated state

Both the console script and the Streamlit GUI call this same function, so chatbot behavior only needs to be updated in one place. The console version prints responses directly in a loop, while the GUI version renders them as chat bubbles and persists state using Streamlit's session state.

## Recognized Commands

| Category | Example input |
|---|---|
| Greeting | `hi`, `hello`, `hey` |
| Name | `my name is Alex` |
| Small talk | `how are you`, `tell me a joke`, `tell me a fact`, `give me a quote`, `give me a compliment` |
| Open talk | `tell me something`, `say something` |
| Utility | `what time is it`, `what day is it`, `calculate 5 + 3` |
| Mood | any message containing words like `happy`, `sad`, `stressed`, etc. |
| Help | `help` |
| Exit | `bye`, `exit`, `quit` |

## Extending the Chatbot

To add a new response rule, open `Code/App.py` and add a new condition inside the `get_response()` function, following the existing pattern:

```python
elif "your_keyword" in user_input:
    return "Chatbot: Your response here.", name, ended
```

Both the console and GUI versions will automatically support the new rule, with no changes needed elsewhere.

## Known Limitations

- Responses are matched using keyword and pattern checks, not natural language understanding, so phrasing outside the recognized patterns will not be understood.
- The built-in calculator uses a restricted `eval()` call intended for local/educational use; it is not hardened for public-facing deployment.
- Conversation state resets when the Streamlit session ends; there is no persistent chat history across sessions.

## License

This project is intended for educational use in demonstrating control flow, decision-making logic, and basic AI concepts.