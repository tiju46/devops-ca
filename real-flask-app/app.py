from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Tiju! Your REAL Flask app is deployed successfully 🚀"

@app.route("/about")
def about():
    return "This is a real Flask application running on AWS EC2 via Docker + Ansible + CI/CD."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
#