from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "OK", 200

@app.route("/hello")
def hello():
    return "Hello OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
