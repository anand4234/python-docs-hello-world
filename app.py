from flask import Flask
app = Flask(__name__)

@app.route("/forms/explore-our-research")
def hello():
    return "Subdomain Takeover PoC by AP :>"
