from flask import Flask, render_template, request, jsonify
from chatbot import ask_question

app = Flask(__name__)

# Home page with chat UI
@app.route("/")
def home():
    return render_template("index.html")

# API endpoint for chatbot
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    
    answer = ask_question(user_input)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
