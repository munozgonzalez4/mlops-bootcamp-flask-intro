'''
This is the main file of the Flask application. It initializes the Flask app and defines the routes for the application.
'''

from flask import Flask

# Create an instance of the Flask class. This instance will be our Web Server Gateway Interface (WSGI) application.
# __name__ is a parameter that Flask uses to determine the root path of the application. It helps Flask to find resources like templates and static files.
app = Flask(__name__)

# Create a basic route for the home page
# The decorator @app.route("/") tells Flask that this function should be called when the root URL ("/") is accessed
@app.route("/")
def welcome():
    return "Welcome to the Flask application! This is a run with debug = True."


# Note: the function name is not important for routing, but it should be unique within the application. The route is determined by the @app.route() decorator, not the function name
@app.route("/index")
def index():
    return "This is the index page."


if __name__ == "__main__":
    app.run(
        debug = True # Server updates automatically when code changes, and provides detailed error messages in the browser. This should be set to False in production for security reasons.
    )