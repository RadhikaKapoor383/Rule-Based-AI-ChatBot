import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Code"))

import streamlit as st
from App import get_response as app_get_response

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
        background-color: #ffffff !important;
    }
    .stChatMessage p, .stChatMessage div, .stChatMessage span {
        color: #1f2a44 !important;
    }
    [data-testid="stChatMessageContent"] {
        color: #1f2a44 !important;
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
        "- `tell me a fact`\n"
        "- `give me a quote`\n"
        "- `give me a compliment`\n"
        "- `what time is it`\n"
        "- `what day is it`\n"
        "- `calculate 5 + 3`\n"
        "- `tell me something`\n"
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

def get_response(raw_text: str) -> str:
    """Wraps App.get_response, syncing Streamlit session state."""
    if st.session_state.conversation_ended:
        return "Our conversation has ended. Click 'Restart conversation' in the sidebar to begin again."

    reply, new_name, ended = app_get_response(
        raw_text,
        name=st.session_state.user_name,
        ended=st.session_state.conversation_ended,
    )

    # App.py replies are prefixed with "Chatbot: " for console use — strip that for the GUI.
    if reply.startswith("Chatbot: "):
        reply = reply[len("Chatbot: "):]

    st.session_state.user_name = new_name
    st.session_state.conversation_ended = ended
    return reply


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