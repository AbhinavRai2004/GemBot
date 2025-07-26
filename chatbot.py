import re
import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import os


load_dotenv()


st.set_page_config(
    page_title="GemBot",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded",
)


st.markdown("""
<style>
    /* General dark theme enhancements */
    .stApp {
        background-color: #0E1117;
    }

    /* Sidebar styling */
    .css-1d391kg {
        background-color: #1a1a2e;
        border-right: 2px solid #3c3c5a;
    }
    
    .css-1d391kg .st-emotion-cache-16txtl3 {
        color: #e0e0ff;
    }

    /* Chat message styling */
    .st-emotion-cache-1c7y2kd {
        border-radius: 20px;
        padding: 1rem 1.25rem;
        margin-bottom: 0.5rem;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        border: 1px solid transparent;
        transition: all 0.3s ease;
    }

    /* User message bubble */
    [data-testid="stChatMessage"]:has([data-testid="stMarkdownContainer"] p) {
        background-color: #252547; /* User message background */
    }

    /* Assistant message bubble */
    [data-testid="stChatMessage"]:has([data-testid="stMarkdownContainer"] p) {
        background-color: #3c3c5a; /* Bot message background */
    }

    /* Input box styling */
    .st-emotion-cache-16txtl3 {
        border-radius: 15px;
        border: 1px solid #3c3c5a;
    }
    
    .stButton>button {
        border-radius: 15px;
        border: 1px solid #3c3c5a;
        background-color: #252547;
    }

</style>
""", unsafe_allow_html=True)


def get_chatbot_response(chat_history):
    """
    Invokes the Gemini model to get a response.
    
    Args:
        chat_history (list): A list of messages representing the conversation history.
        
    Returns:
        str: The content of the AI's response.
    """
    try:
        huggingface_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        if not huggingface_api_key:
            st.error("HuggingFace API Key not found. Please set it in the .env file.")
            return None

        llm = HuggingFaceEndpoint(
                     repo_id="deepseek-ai/DeepSeek-R1-0528",
                     task="text-generation"
        )
        model = ChatHuggingFace(llm = llm)

        output = model.invoke(chat_history)
        return output.content
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "Sorry, I encountered an error. Please try again."


with st.sidebar:
    st.title("✨GemBot Chatbot")
    st.markdown("""
    Welcome to your personal AI assistant powered by Deepseek's R1-0528 model.
    
    **Instructions:**
    1.  Type your message in the chat box below.
    2.  Press Enter or click the send button.
    3.  The conversation history is remembered for a continuous chat experience.
    """)
    st.info("This is a demo application. Your chat history is stored only for the current session.")

st.header("Chat with GemBot")


if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content='You are a helpful and friendly AI assistant.'),
        AIMessage(content='Hello! How can I assist you today?'),
    ]


for message in st.session_state.chat_history:
    if isinstance(message, SystemMessage):
        continue
        
    role = "assistant" if isinstance(message, AIMessage) else "user"
    with st.chat_message(role):
        st.markdown(message.content)


user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to history and display it
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.markdown(user_input)
   
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_chatbot_response(st.session_state.chat_history)
            cleaned_response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL)
            st.markdown(cleaned_response.strip())
    

    st.session_state.chat_history.append(AIMessage(content=cleaned_response.strip()))