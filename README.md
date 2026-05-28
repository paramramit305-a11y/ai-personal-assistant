<div align="center">

# 🤖 AI Personal Assistant

### A Flask-powered AI web app for answering questions & summarizing emails — deployed with Groq's lightning-fast LLM API

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_4_Scout-F55036?style=for-the-badge&logoColor=white)](https://groq.com)
[![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

### 🌐 [Live Demo](https://ai-personal-assistant-u5wj.onrender.com)

</div>

---

## 📌 Overview

**AI Personal Assistant** is a lightweight web application built with **Flask** and deployed on **Render**, powered by the **Groq API (Llama 4 Scout 17B)**. It delivers fast, intelligent responses through a clean, minimal UI — no heavy frameworks, no unnecessary complexity.

The app supports two core use cases:

- 💬 **Ask Anything** — Get instant, intelligent answers to any question
- 📧 **Email Summarizer** — Paste any email, get a clean 2-3 sentence summary

> 💡 Built as part of learning Flask deployment with real-world LLM integration using the OpenAI-compatible Groq SDK.

---

## 🎯 Problem Statement

Most AI tools are either too heavy to deploy or too complex to build from scratch. This project demonstrates how a fully functional AI web app can be built with minimal tools — just Flask + Groq API — and deployed live in under an hour.

---

## 🏗️ Architecture

```
                        REQUEST FLOW
─────────────────────────────────────────────────────
  User (Browser)
      │
      ▼
┌─────────────────┐
│   index.html    │  ← Frontend UI (HTML + CSS)
│   (Jinja2)      │    Async fetch() for API calls
└────────┬────────┘
         │  POST /ask  or  POST /summarize
         ▼
┌─────────────────┐
│   Flask App     │  ← main.py
│   (main.py)     │    Routes: /, /ask, /summarize
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Groq API      │  ← OpenAI-compatible SDK
│  LLaMA 4 Scout  │    chat.completions.create()
│    (17B)        │
└────────┬────────┘
         │
         ▼
   JSON Response → Browser
```

---

## 🛠️ Tech Stack

<div align="center">

| Component | Technology |
|:----------|:-----------|
| 🌐 Backend | Flask (Python) |
| 🤖 LLM | Groq — `meta-llama/llama-4-scout-17b-16e-instruct` |
| 🔗 SDK | OpenAI-compatible Groq SDK |
| 🎨 Frontend | HTML5, CSS3 (Vanilla) |
| ⚙️ Config | python-dotenv |
| 🚀 Deployment | Render.com (Free tier) |
| 🐍 Language | Python 3.10+ |

</div>

---

## 📁 Project Structure

```
ai-personal-assistant/
│
├── main.py                  # Flask app & API routes
├── templates/
│   └── index.html           # Frontend UI (Jinja2)
├── static/
│   └── style.css            # Styling
├── openai_api.ipynb         # Groq API experiments & exploration
├── requirements.txt         # Python dependencies
├── .gitignore
└── .env                     # API keys (not committed)
```

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|:-------|:---------|:------------|
| `GET` | `/` | Serves the main UI |
| `POST` | `/ask` | Accepts a question → returns AI answer |
| `POST` | `/summarize` | Accepts email text → returns summary |

---

## 🚀 Setup & Run

**1. Clone the repository**
```bash
git clone https://github.com/paramramit305-a11y/ai-personal-assistant.git
cd ai-personal-assistant
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up environment variables**
```bash
# Create .env file in root directory
GROQ_API_KEY=your_groq_api_key_here
```

> 🔑 Get your free API key at [console.groq.com](https://console.groq.com)

**4. Run the app**
```bash
python main.py
```

Open `http://127.0.0.1:5000` in your browser ✅

---

## 🧪 Example Usage

```python
# Ask Anything
POST /ask
body: { "question": "Explain transformers in simple words" }

# Summarize Email
POST /summarize
body: { "email": "Hi, I wanted to share an update about the project..." }
```

---

## 📊 Key Design Decisions

| Decision | Reason |
|:---------|:-------|
| Groq over OpenAI | Free tier, faster inference (600+ tokens/sec) |
| Llama 4 Scout 17B | Multimodal, 2x faster than Llama 3.3 70B |
| Vanilla CSS | No framework overhead, full control |
| Async fetch() | Non-blocking UI — no page reload on submit |
| Gunicorn on Render | Production-grade WSGI server |

---

## 🔮 Future Improvements

- [ ] Add conversation history (multi-turn chat)
- [ ] Image understanding feature (Llama 4 Scout is multimodal)
- [ ] Add more tools — code explainer, tweet generator
- [ ] Add loading animation / streaming response
- [ ] User authentication

---

## 👤 Author

<div align="center">

**Parmar Amit**
*BSc IT (AIML) | Gokul Global University*

[![GitHub](https://img.shields.io/badge/GitHub-paramramit305--a11y-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/paramramit305-a11y)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Parmar%20Amit-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/parmar-amit-97941a377)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-parmar--amit-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/parmar-amit)

</div>

---

<div align="center">

⭐ If you found this useful, consider starring the repo!

</div>
