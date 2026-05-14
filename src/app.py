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
    return "Welcome to the Flask application!"


if __name__ == '__main__':
    app.run()