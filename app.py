from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "proxy running"

@app.route("/fetch")
def fetch():
    url = request.args.get("url")
    if not url:
        return {"error": "missing url"}, 400

    try:
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept-Language": "en-US,en;q=0.9"
        }

        resp = requests.get(url, headers=headers, timeout=15)

        return Response(
            resp.content,
            status=resp.status_code,
            content_type=resp.headers.get("Content-Type", "text/html")
        )

    except Exception as e:
        return {"error": str(e)}, 500
