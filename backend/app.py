from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# You'll set your OpenAI key as an environment variable on Render later.
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/explain", methods=["POST"])
def explain():
    data = request.get_json()
    sentence = data.get("sentence", "")

    if not sentence:
        return jsonify({"error": "No sentence provided"}), 400

    # You can refine this prompt later.
    prompt = f"Explain the Estonian grammar in this sentence: {sentence}\nProvide a clear English breakdown for each word."

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    explanation = response.choices[0].message.content
    return jsonify({"explanation": explanation})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
