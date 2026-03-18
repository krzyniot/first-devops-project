from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

VERSION = "5.0"

REQUEST_COUNT = Counter("app_requests_total", "Total requests")

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return f"DevOps Project Krzysztof Trojańczuk - version {VERSION}"

@app.route("/health")
def health():
    return "OK"

@app.route("/version")
def version():
    return VERSION

from flask import Response

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
