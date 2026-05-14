"""
Objective: To understand the difference between GET and POST requests in web development and integrate into the Flask framework.

Get request: A GET request is used to retrieve data from a server. When a client sends a GET request, it is asking the server to send back the requested resource. 
The server processes the request and returns the appropriate response, which typically includes the requested data.

Post request: A POST request is used to send data to a server to create or update a resource. 
When a client sends a POST request, it includes data in the body of the request, which the server processes and uses to create or update the specified resource. 
The server then returns a response indicating the success or failure of the operation.
"""

# Adding request to the imports to handle incoming data from POST requests
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the GET and POST request example!"

# The index route is accessible via a GET request, and it renders the index.html template
@app.route("/index", methods = ["GET"])
def index():
    return render_template("index.html")

# The form route is accessible via a POST request, and it processes the form data submitted by the user.
# If the request method is POST, it retrieves the name from the form data and returns a greeting message. 
# If the request method is GET, it renders the form.html template for the user to fill out.
@app.route("/form", methods = ["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}! Your form has been submitted successfully."
    return render_template("form.html") # Render the form template for GET requests


# In the html file, we have set the form action to "/submit", so we need to create a route for "/submit" to handle the form submission
@app.route("/submit", methods = ["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        return f"Hello, {name}!"
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)