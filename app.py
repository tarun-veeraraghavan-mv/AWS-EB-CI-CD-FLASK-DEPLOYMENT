from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "OK", 200

@app.route("/hello")
def hello():
    return "Hello OK", 200

@app.route("/new-route")
def aws_works():
    return "If this works - AWS CI/CD works!"

secret = os.getenv('AWS_SECRET')

@app.route("/secret")
def check_aws_secret_works():
    return f"Secret works or not: {secret}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
