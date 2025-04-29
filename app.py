from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # הוספת התמיכה ב-CORS


openai.api_key = os.getenv("OPENAI_API_KEY", "sk-...")

@app.route('/check_phishing', methods=['POST'])
def check_phishing():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Missing text"}), 400

    prompt = f"""
האם הטקסט הבא הוא הודעת פישינג? הסבר בעברית בקצרה:
1. האם זו נראית הודעת פישינג (כן/לא)?
2. הסבר למה.
3. מה הסיכון?

טקסט:
\"\"\"{text}\"\"\"
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "אתה מומחה אבטחת מידע ועוזר בזיהוי הונאות."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        answer = response.choices[0].message.content.strip()
        return jsonify({"result": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
