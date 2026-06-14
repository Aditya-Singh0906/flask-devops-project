from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to DevOps!</h1>
    <p>My first DevOps project using Flask, Docker, GitHub Actions and AWS EC2.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)