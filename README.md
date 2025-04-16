# Sentiment Analyzer – AI App using Mistral, FastAPI & Streamlit

This is a sentiment analysis web app that uses a **locally hosted Mistral LLM via Ollama**, with a **FastAPI backend** and **Streamlit frontend**.

## Demo

*Watch the [Sentiment Analyzer demo video](https://youtu.be/Lcd6b1LUXLc) to see it in action.*

---

## Features

- **Input text** and get instant AI-driven sentiment analysis
- **Runs offline** using Mistral via Ollama (no cloud API)
- Built with:
  - **FastAPI** (backend API)
  - **Streamlit** (modern UI)
  - **Ollama + Mistral** (local LLM inference)

---

## Installation

```bash
git clone https://github.com/yourusername/sentiment-analyzer-mistral.git
cd sentiment-analyzer-mistral
python -m venv venv
venv\Scripts\activate  # On Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
