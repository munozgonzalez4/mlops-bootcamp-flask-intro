"""
Objective: integrate HTML tags
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the Flask course</H1></html>"


if __name__ == "__main__":
    app.run(
        debug = True
    )