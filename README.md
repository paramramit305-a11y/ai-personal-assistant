<div align="center">

# 🤖 AI Personal Assistant

### A Flask-powered AI assistant for answering questions & summarizing emails — built with Groq's lightning-fast LLM API

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_4_Scout-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Overview

**AI Personal Assistant** is a lightweight web application built with Flask that leverages the **Groq API (Llama 4 Scout 17B)** to deliver fast, intelligent responses. It supports two core use cases:

- 💬 **Ask Anything** — Get instant answers to any question
- 📧 **Email Summarizer** — Paste any email, get a clean 2-3 sentence summary

---

## ✨ Features

| Feature | Description |
|---|---|
| ⚡ Fast Inference | Powered by Groq — one of the fastest LLM inference APIs |
| 🧠 Smart Answers | Uses `llama-4-scout-17b` for high-quality responses |
| 📧 Email Summary | Summarizes long emails into 2-3 actionable sentences |
| 🎨 Clean UI | Minimal, professional frontend — no frameworks needed |
| 🔒 Secure | API key stored in `.env`, never exposed |

---

## 🛠️ Tech Stack

```
Backend     →  Python, Flask
AI Model    →  meta-llama/llama-4-scout-17b-16e-instruct (via Groq API)
Frontend    →  HTML5, CSS3 (Vanilla)
Config      →  python-dotenv
Deploy      →  Render.com
```

---

## 📁 Project Structure

```
ai-personal-assistant/
├── main.py                  # Flask app & API routes
├── templates/
│   └── index.html           # Frontend UI
├── static/
│   └── style.css            # Styling
├── requirements.txt         # Python dependencies
├── .gitignore
└── .env                     # API keys (not committed)
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/paramramit305-a11y/ai-personal-assistant.git
cd ai-personal-assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```
> 🔑 Get your free API key at [console.groq.com](https://console.groq.com)

### 4. Run the app
```bash
python main.py
```

Open `http://127.0.0.1:5000` in your browser ✅

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serves the main UI |
| `POST` | `/ask` | Accepts a question, returns AI response |
| `POST` | `/summarize` | Accepts email text, returns summary |

---

## 👤 Author

**Amit Parmar**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/parmar-amit-97941a377)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github)](https://github.com/paramramit305-a11y)

---

<div align="center">
⭐ If you found this useful, consider starring the repo!
</div>
