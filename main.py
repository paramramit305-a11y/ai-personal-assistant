from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from openai import OpenAI

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")


client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")
        
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "Act like a helpful personal assistant"},
            {"role": "user", "content": question}
        ],
        temperature=0.7,
        max_tokens=512
    )

    answer = response.choices[0].message.content.strip()
    return jsonify({"response": answer}), 200


@app.route("/summarize", methods=["POST"])
def summarize():
    email_text = request.form.get("email")
    prompt = f"summarize the following email in 2-3 sentences with useful information: {email_text}"
        
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "Act like an expert email assistant"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=512
    )

    summary = response.choices[0].message.content.strip()
    return jsonify({"response": summary}), 200



if __name__ == "__main__":
    app.run(debug=True)
