from flask import Flask

app = Flask(__name__)

VERSION = "1.0"

@app.route("/")
def home():
    return f"DevOps Project - version {VERSION}"

@app.route("/health")
def health():
    return "OK"

@app.route("/version")
def version():
    return VERSION

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
