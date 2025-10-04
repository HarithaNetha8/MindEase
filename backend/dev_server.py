"""Lightweight development server that mimics the Flask API without external deps.

Run with: python dev_server.py
"""
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse


def supportive_message(label: str):
    label = (label or "").upper()
    if label == "NEGATIVE":
        return (
            "That sounds tough. I'm here for you. "
            "Try a 4-7-8 breathing cycle: inhale 4s, hold 7s, exhale 8s. "
            "Want a journaling prompt?"
        )
    elif label == "POSITIVE":
        return (
            "Love that! Celebrate the win and note what worked today. "
            "Would you like a quick gratitude prompt?"
        )
    else:
        return (
            "Got it. Thanks for sharing. "
            "How about a 60-second check-in: body scan and a deep breath?"
        )


class DevHandler(BaseHTTPRequestHandler):
    def _set_json(self, status=200):
        self.send_response(status)
        # Allow cross-origin requests for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path
        if path == '/api/health':
            self._set_json(200)
            self.wfile.write(json.dumps({'ok': True}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        path = urlparse(self.path).path
        if path != '/api/analyze':
            self.send_response(404)
            self.end_headers()
            return

        # Read JSON body
        length = int(self.headers.get('Content-Length', '0'))
        body = self.rfile.read(length).decode('utf-8') if length else ''
        try:
            data = json.loads(body) if body else {}
        except Exception:
            data = {}

        text = (data.get('message') or '').strip()
        if not text:
            self._set_json(400)
            self.wfile.write(json.dumps({'error': 'message is required'}).encode())
            return

        lower = text.lower()
        # simple cues
        pos_words = ['good', 'great', 'happy', 'love', 'awesome', 'thanks', 'thank']
        neg_words = ['not', 'sad', 'bad', 'hate', 'angry', 'upset', 'terrible', 'depressed']
        # emoji cues
        pos_emoji = ['😊', '😄', '🙂', ':)', ':-)']
        neg_emoji = ['😔', '😢', '😞', ':(', ':-(']

        pos_score = sum(lower.count(w) for w in pos_words) + sum(text.count(e) for e in pos_emoji)
        neg_score = sum(lower.count(w) for w in neg_words) + sum(text.count(e) for e in neg_emoji)

        # length / exclamation nudges
        if '!' in text and pos_score >= neg_score:
            pos_score += 1
        if len(text.split()) > 6:
            # give a slight nudge to detected sentiment for longer messages
            pos_score += 0.2 * pos_score
            neg_score += 0.2 * neg_score

        if neg_score > pos_score:
            label = 'NEGATIVE'
            score = min(0.95, 0.5 + neg_score * 0.15)
        elif pos_score > neg_score:
            label = 'POSITIVE'
            score = min(0.95, 0.5 + pos_score * 0.15)
        else:
            # short greetings get a friendly response rather than neutral
            if lower in ('hi', 'hii', 'hey', 'hello') or len(text) <= 3:
                label = 'POSITIVE'
                score = 0.55
            else:
                label = 'NEUTRAL'
                score = 0.5

        reply = supportive_message(label)
        self._set_json(200)
        self.wfile.write(json.dumps({'label': label, 'score': score, 'reply': reply}).encode())

    def do_OPTIONS(self):
        # Respond to preflight CORS requests with no body
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()


def run(host='127.0.0.1', port=5000):
    print(f'Development server running on http://{host}:{port}')
    server = HTTPServer((host, port), DevHandler)
    server.serve_forever()


if __name__ == '__main__':
    run()
