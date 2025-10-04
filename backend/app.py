from flask import Flask, request, jsonify
from flask_cors import CORS
try:
    from transformers import pipeline
except Exception:
    pipeline = None  # type: ignore


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Lazily create sentiment pipeline if available, otherwise use a simple fallback
if pipeline is not None:
    try:
        sentiment = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english",
        )
    except Exception:
        sentiment = None
else:
    sentiment = None

def supportive_message(label: str):
    label = (label or "").upper()
    if label == "NEGATIVE":
        return ("That sounds tough. I'm here for you. "
                "Try a 4-7-8 breathing cycle: inhale 4s, hold 7s, exhale 8s. "
                "Want a journaling prompt?")
    elif label == "POSITIVE":
        return ("Love that! Celebrate the win and note what worked today. "
                "Would you like a quick gratitude prompt?")
    else:
        return ("Got it. Thanks for sharing. "
                "How about a 60-second check-in: body scan and a deep breath?")

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"ok": True})

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json(force=True) or {}
    text = data.get("message", "").strip()
    if not text:
        return jsonify({"error": "message is required"}), 400
    # If model is available, use it. Otherwise return a simple neutral reply for dev.
    if sentiment:
        res = sentiment(text)[0]  # {"label": "...", "score": ...}
        label = res.get("label")
        score = float(res.get("score", 0))
    else:
        # Basic heuristic fallback
        lower = text.lower()
        if any(w in lower for w in ["not", "sad", "bad", "hate", "angry", "upset"]):
            label = "NEGATIVE"
            score = 0.6
        elif any(w in lower for w in ["good", "great", "happy", "love", "awesome"]):
            label = "POSITIVE"
            score = 0.7
        else:
            label = "NEUTRAL"
            score = 0.5

    reply = supportive_message(label)
    return jsonify({
        "label": label,
        "score": score,
        "reply": reply
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
