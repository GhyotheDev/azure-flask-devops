from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Azure DevOps Demo  🚀</h1><p>This app is deployed using Azure CI/CD methodologies .</p>"

@app.route("/health")
def health():
    return {"status": "healthy and ready for action!"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
