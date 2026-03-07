import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

# Initialize Groq client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

st.set_page_config(page_title="Groq Chat App", page_icon="🚀")

st.title("🚀 Groq LLM Chat")
st.write("Powered by Groq API")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are an assistant."}
    ]

# Display previous messages
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Enter your prompt...")

if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from Groq
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama3-70b-8192",  # Recommended Groq model
                messages=st.session_state.messages,
                temperature=0.7
            )

            reply = response.choices[0].message.content
            st.markdown(reply)

    # Store assistant reply
    st.session_state.messages.append({"role": "assistant", "content": reply})