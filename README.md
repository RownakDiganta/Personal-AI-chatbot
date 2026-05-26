# 🤖 Personal AI Chatbot

A conversational AI chatbot built using **Streamlit**, **LangChain**, and **OpenAI**.  
This project provides a clean chat interface with persistent conversation memory, allowing users to interact naturally with an AI assistant.

---

## 🚀 Features

- 💬 Interactive chat interface using Streamlit
- 🧠 Conversation memory using LangChain
- 🤖 Powered by OpenAI GPT models
- 🗂 Persistent chat history during session
- 🔄 Clear chat history functionality
- 🎨 Custom chatbot icon and responsive UI
- ⚡ Fast and lightweight implementation

---

## 🛠 Tech Stack

### Frontend
- Streamlit

### Backend / AI
- LangChain
- OpenAI API

### Memory Handling
- ConversationBufferMemory

### Environment Management
- python-dotenv

---

## 📂 Project Structure

```bash
Personal-AI-chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── logo.png
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/RownakDiganta/Personal-AI-chatbot.git
```

### 2. Navigate into the project

```bash
cd Personal-AI-chatbot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

#### macOS/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser automatically.

---

## 🧠 How It Works

The chatbot uses:

- **ChatOpenAI** for generating responses
- **ConversationChain** to manage interactions
- **ConversationBufferMemory** to remember previous messages
- **Streamlit session state** for maintaining chat history

---

## 📦 Dependencies

Main libraries used:

- streamlit
- openai
- langchain
- python-dotenv
- numpy
- pandas

---

## 📸 UI Preview

Features included in the interface:

- Chat bubbles for user and assistant
- Sidebar options
- Chat history reset button
- Custom chatbot branding

---

## 👨‍💻 Author

**Md Rownak Abtahee Diganta**

- Simon Fraser University
- Computing Science (Honours) + Statistics Minor
- Interests: AI, Machine Learning, Data Science, LLM Applications


