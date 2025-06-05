from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "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"  

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"response": "No prompt received"}), 400

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        return jsonify({"response": completion.choices[0].message['content']})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
