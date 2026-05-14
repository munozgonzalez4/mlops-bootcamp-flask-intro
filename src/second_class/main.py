"""
Objective: integrate HTML tags
"""

from flask import Flask, render_template

app = Flask(__name__)

# Manual way to integrate HTML tags: not recommended
@app.route("/")
def welcome():
    return "<html><H1>Welcome to the Flask course</H1></html>"


# Using templates to integrate HTML tags: recommended way
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(
        debug = True
    )