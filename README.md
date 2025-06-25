# Gemini Chatbot – Streamlit + LangChain Interface

A privacy-focused chatbot interface built using Python, Streamlit, and LangChain, powered by Google's Gemini 1.5 Flash model.

## 🧠 Project Overview

This project demonstrates how to build a lightweight conversational AI interface using [LangChain](https://www.langchain.com/) and [Streamlit](https://streamlit.io/). It leverages the Gemini 1.5 Flash model via Google's Generative AI API to respond to user queries in real-time.

LangChain is used to structure the chat history and manage message flow, making the interaction feel natural and extensible.

## ✅ Features

- Clean chatbot UI built with Streamlit
- Gemini 1.5 Flash integration via LangChain
- Maintains full chat history in session memory
- Download options for:
  - Full conversation
  - Specific query-response pairs
- Clear chat history button
- Fully local and privacy-respecting (no data storage)

## 🔧 Technologies Used

- Python
- Streamlit (UI)
- LangChain (chat history, message modeling)
- Google Generative AI API (Gemini 1.5 Flash)
- Python Dotenv (`.env` file for secrets)

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gemini-chatbot-langchain.git
cd gemini-chatbot-langchain
