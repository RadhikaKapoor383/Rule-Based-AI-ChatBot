"""
Rule-Based Chatbot — Streamlit Interface
Run with: streamlit run chatbot_app.py
"""

import random
import datetime
import streamlit as st

# ----------------------------------------------------------------------------
# Page configuration
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Aria - Rule-Based Assistant",
    page_icon=":material/smart_toy:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# Custom styling (professional look)
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f6fa;
    }
    .main .block-container {
        padding-top: 2rem;
        max-width: 760px;
    }
    .chat-header {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 16px 20px;
        background: #1f2a44;
        border-radius: 12px;
        margin-bottom: 18px;
    }
    .chat-header h1 {
        color: #ffffff;
        font-size: 20px;
        font-weight: 600;
        margin: 0;
    }
    .chat-header p {
        color: #b9c2d6;
        font-size: 13px;
        margin: 0;
    }
    .bot-icon {
        width: 36px;
        height: 36px;
        border-radius: 8px;
        background-color: #324a73;
        color: #ffffff;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 14px;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    .status-dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background-color: #2ecc71;
        display: inline-block;
        margin-right: 6px;
    }
    .stChatMessage {
        border-radius: 10px;
    }
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Sidebar
# ----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### About this assistant")
    st.write(
        "This is a rule-based chatbot built with simple if-else logic. "
        "It recognizes a fixed set of intents (greetings, name capture, "
        "small talk, jokes, time, and exit commands)."
    )
    st.markdown("---")
    st.markdown("**Try saying:**")
    st.markdown(
        "- `hi` / `hello`\n"
        "- `my name is ...`\n"
        "- `how are you`\n"
        "- `tell me a joke`\n"
        "- `what time is it`\n"
        "- `help`\n"
        "- `bye` / `exit`"
    )
    st.markdown("---")
    if st.button("Restart conversation", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# ----------------------------------------------------------------------------
# Header
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="chat-header">
        <div class="bot-icon">AI</div>
        <div>
            <h1>Aria</h1>
            <p><span class="status-dot"></span>Online - Rule-based assistant</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# State initialization
# ----------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I'm Aria, a rule-based assistant. What's your name?",
        }
    ]
if "user_name" not in st.session_state:
    st.session_state.user_name = None
if "conversation_ended" not in st.session_state:
    st.session_state.conversation_ended = False

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "I told my computer I needed a break, and it said no problem — it'll sleep too.",
    "Why was the JavaScript developer sad? Because they didn't know how to null their feelings.",
    "Why do Python programmers wear glasses? Because they can't C.",
]

# ----------------------------------------------------------------------------
# Rule-based response engine
# ----------------------------------------------------------------------------
def get_response(raw_text: str) -> str:
    text = raw_text.strip()
    lower = text.lower()
    name = st.session_state.user_name

    if st.session_state.conversation_ended:
        return "Our conversation has ended. Click 'Restart conversation' in the sidebar to begin again."

    if lower == "":
        return "Please type something so I can respond."

    if lower.startswith(("hi", "hello", "hey")):
        return f"Hello again, {name}!" if name else "Hello there! What's your name?"

    if lower.startswith(("my name is", "i am", "i'm")):
        parts = lower.replace("i'm", "my name is").replace("i am", "my name is")
        candidate = parts.split("my name is", 1)[1].strip(" .!")
        if candidate:
            st.session_state.user_name = candidate.capitalize()
            return f"Nice to meet you, {st.session_state.user_name}! How can I help you today?"
        return "I didn't quite catch that — could you repeat your name?"

    if "how are you" in lower:
        return f"I'm doing great, thanks for asking{', ' + name if name else ''}!"

    if "your name" in lower or "who are you" in lower:
        return "I'm Aria, a simple rule-based chatbot built to demonstrate control flow and decision logic."

    if "joke" in lower:
        return random.choice(JOKES)

    if "time" in lower:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."

    if "weather" in lower:
        return "I can't check live weather in this demo, but a production chatbot could call a weather API here."

    if "thank" in lower:
        return f"You're welcome{', ' + name if name else ''}!"

    if "help" in lower:
        return "You can greet me, tell me your name, ask for a joke or the time, or say 'bye' to exit."

    if lower.startswith(("bye", "exit", "quit")):
        st.session_state.conversation_ended = True
        return f"Goodbye{', ' + name if name else ''}! It was nice chatting with you."

    return "Sorry, I don't understand that yet. Try 'help' to see what I can do."


# ----------------------------------------------------------------------------
# Render chat history
# ----------------------------------------------------------------------------
for msg in st.session_state.messages:
    avatar = ":material/person:" if msg["role"] == "user" else ":material/smart_toy:"
    with st.chat_message(msg["role"], avatar=avatar):
        st.write(msg["content"])

# ----------------------------------------------------------------------------
# Chat input
# ----------------------------------------------------------------------------
placeholder = "Type your message..." if not st.session_state.conversation_ended else "Conversation ended"
user_input = st.chat_input(placeholder, disabled=st.session_state.conversation_ended)

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar=":material/person:"):
        st.write(user_input)

    reply = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant", avatar=":material/smart_toy:"):
        st.write(reply)