# Rule-Based AI Chatbot

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-GUI-red)
![AI](https://img.shields.io/badge/AI-Rule--Based-green)
![Status](https://img.shields.io/badge/Status-Active-success)

A simple yet interactive **rule-based AI chatbot** that responds to predefined user inputs using conditional logic and control flow. The chatbot is implemented in both a **command-line interface (CLI)** and an interactive **Streamlit web application**.

The project demonstrates fundamental AI concepts, conversational logic, and state management using Python.

**Live Demo**: https://aria-ai-chatbot.streamlit.app/ </br>
**GitHub Repository**: https://github.com/RadhikaKapoor383/Rule-Based-AI-ChatBot

---

## Project Overview

This chatbot simulates human conversation through predefined rules and intent matching. It can recognize greetings, respond to common questions, perform calculations, provide motivational content, and maintain simple conversation state.

The application is available in two versions:

* Console-based chatbot
* Streamlit web interface

---

## Features

* Greeting recognition (`hi`, `hello`, `hey`)
* Personalized conversations with name detection
* Mood and sentiment-aware responses
* Jokes, quotes, compliments, and facts
* Built-in arithmetic calculator
* Current date and time lookup
* Open-ended small talk support
* Conversation summary on exit
* Continuous interaction until termination
* Interactive Streamlit GUI

---

## Technologies Used

* Python
* Streamlit
* Conditional Logic
* State Management
* Date & Time Module

---

## Project Structure

```text
Rule-based-AI-chatbot/
│
├── Code/
│   └── App.py
│
├── Gui/
│   ├── chatbot-gui.py
│   └── .streamlit/
│       └── config.toml
│
├── .gitignore
└── README.md
```

---

## Features Supported

| Category         | Examples                       |
| ---------------- | ------------------------------ |
| Greeting         | hi, hello, hey                 |
| Name Recognition | my name is Alex                |
| Small Talk       | how are you, tell me a joke    |
| Motivation       | give me a quote, compliment    |
| Utility          | calculate 5+3, what time is it |
| Mood Detection   | happy, sad, stressed           |
| Help             | help                           |
| Exit             | bye, quit, exit                |

---

## Installation

### Clone the repository

```bash
git clone https://github.com/RadhikaKapoor383/Rule-based-AI-chatbot.git
```

### Install dependencies

```bash
pip install streamlit
```

---

## Run the Console Version

```bash
cd Code
python App.py
```

---

## Run the Streamlit Version

```bash
cd Gui
streamlit run chatbot-gui.py
```

The application will launch in your browser at:

```text
http://localhost:8501
```

---

## How It Works

1. User enters a message.
2. The chatbot analyzes keywords and patterns.
3. The appropriate rule is matched.
4. A predefined response is generated.
5. Conversation state is maintained throughout the session.

Both the console and GUI applications use the same response engine, ensuring consistent behavior.

---

## Extending the Chatbot

New rules can easily be added inside the `get_response()` function:

```python
elif "your_keyword" in user_input:
    return "Your response here."
```

The new response automatically becomes available in both the console and GUI versions.

---

## Limitations

* Uses rule-based logic instead of Natural Language Processing.
* Limited to predefined patterns and keywords.
* Conversation history is not permanently stored.
* Calculator functionality is intended for educational purposes.

---

## Future Improvements

* Integrate NLP techniques.
* Add voice interaction.
* Support multiple languages.
* Store chat history in a database.
* Integrate AI APIs for advanced conversations.

---

## Author

**Radhika Kapoor**
BS Computer Science Student
Sukkur IBA University

* GitHub: https://github.com/RadhikaKapoor383
* LinkedIn: https://www.linkedin.com/in/radhika-kapoor2005/

---

## License

This project is developed for educational purposes to demonstrate decision-making logic, control flow, and introductory AI concepts.

---

If you found this project useful, consider giving it a star on GitHub.
