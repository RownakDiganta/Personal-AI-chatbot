import streamlit as st
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, AIMessage
from PIL import Image

load_dotenv()

icon = Image.open("logo.png")

st.set_page_config(
    page_title="My Personal AI chatbot",
    page_icon= icon,
    layout="centered")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image(icon, width=220)
    
st.title("My Personal AI chatbot")
st.subheader("A chatbot that can answer your questions and have a conversation with you. Powered by streamlit, langchain and openai.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "conversation" not in st.session_state:
    llm = ChatOpenAI(
        model_name = "gpt-5.4-mini", 
        temperature = 0.7,
        openai_api_key = os.getenv("OPENAI_API_KEY")
    )
    
    memory = ConversationBufferMemory(
        return_messages = True
    )
    
    st.session_state.conversation = ConversationChain(
        llm = llm,
        memory = memory,
        verbose = False
    )
    
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    else:
        with st.chat_message("assistant"):
            st.write(message.content)

user_input = st.chat_input("Type your message here...")

if user_input:

    st.session_state.chat_history.append(
        HumanMessage(content=user_input)
    )

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.conversation.predict(
                input=user_input
            )
            st.write(response)
            
    st.session_state.chat_history.append(
        AIMessage(content=response)
    )

with st.sidebar:
    
    st.title("Options")

    if st.button("Clear Chat History"):
        st.session_state.chat_history = []

        memory = ConversationBufferMemory(return_messages=True)

        llm = ChatOpenAI(
            model_name = "gpt-5.4-mini",
            temperature = 0.7,
            openai_api_key = os.getenv("OPENAI_API_KEY")
        )

        st.session_state.conversation = ConversationChain(
            llm = llm,
            memory = memory,
            verbose = False
        )

        st.rerun()

    st.subheader("About")
    
    st.markdown(
    """
    Author: Md Rownak Abtahee Diganta
    
    This chatbot uses:

    - **Streamlit** for the web interface
    - **LangChain** for the conversation management
    - **GPT-5.4-mini** as the language model
    - **ConversationBufferMemory** to remember previous messages
    """
    )

