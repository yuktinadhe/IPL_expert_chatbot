# 🏏 IPL Chatbot (RAG + Gemini API)

An **AI-powered chatbot** trained on **1000 IPL Q&A pairs**.  
It uses **RAG (Retrieval-Augmented Generation)** with FAISS + LangChain + Google Gemini API.

## 🚀 Features
- Ask **any IPL-related question** and get accurate answers.
- Built using **Flask + LangChain + Gemini API**.
- Frontend with a clean **chat UI** (HTML, CSS, JS).
- Uses **PDF dataset (1000 IPL QAs)** as knowledge base.
- Easy to extend with more datasets.

## 📂 Project Structure
ipl_chatbot/
│── data/
│ └── IPL_QA_Dataset.pdf # Knowledge base (PDF)
│── app.py # Flask backend
│── chatbot.py # Core chatbot logic (PDF + Gemini API)
│── templates/
│ └── index.html # Simple chat UI
│── requirements.txt # Python dependencies
│── .gitignore # Ignored files (.env, pycache)

## ⚡ Features

- Ask IPL-related questions 🏏
- Uses PDF dataset + Gemini API
- Simple chatbox UI (HTML + Flask)
- Secure API keys with .env
- Easy to run locally

## 🖼️ Demo Screenshot
<img width="1915" height="965" alt="image" src="https://github.com/user-attachments/assets/c036c917-e6e6-4bf5-9d12-986bc80c2d82" />

## 🛠️ Tech Stack
Backend: Flask
Frontend: HTML, CSS
LLM: Google Gemini
Data Source: IPL_QA_Dataset.pdf

## 👨‍💻 Author

Built with ❤️ by Yukti Nadhe
