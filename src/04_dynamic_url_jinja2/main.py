"""
Build URLs dynamically with Jinja2 templates.
Main idea: use Jinja2 to create URL templates that can be filled with dynamic data at runtime.
Important concept: Variable Rule - parameters in the URL that can be passed to the function. This allows us to create dynamic URLs that can accept different values and generate responses based on those values.
"""

# redirect: used to redirect the user to a different route. This is useful when we want to direct the user to a different page based on some conditions or after a form submission.
# url_for: used to generate URLs dynamically based on the parameters passed to the function. 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Dynamic URL Builder!"


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        return f"Hello, {name}! Your form has been submitted."
    return render_template("form.html")


# Variable Rule: parameters in the URL that can be passed to the function
# Note the use of <int:score> - this means that the score parameter will be treated as an integer.
# If the user tries to access /success/some_string, it will result in a 404 error because the URL expects an integer.
@app.route("/success/<int:score>")
def success(score):
    return f"Your score is: {score * 1.0}"

# Dynamic URL with Jinja2 template: we can use the render_template function to pass variables to the template and create dynamic content based on the result
@app.route("/success_v2/<int:score>")
def success_v2(score):
    if score >= 90:
        res = "Excellent!"
    else:
        res = "Keep trying!"
    return render_template("result_v2.html", result = res)


"""
Jinja 2 template expressions:
- {{ }}: used to evaluate and print the result of an expression. For example, {{ result }} will print the value of the variable result.
- {%...%}: used for control statements like loops and conditionals. For example, {% if score >= 90 %} will check if the score is greater than or equal to 90 and execute the block of code inside the if statement.
- {#...#}: used for comments. Anything inside these tags will be ignored by the template engine and will not be rendered in the final output.
"""

# Result as dictionary: we can pass a dictionary to the template and access its values using the keys. This allows us to organize our data in a more structured way and makes it easier to manage complex data.
# The template will include a for loop to iterate over the dictionary and display the key-value pairs in a formatted way.
@app.route("/success_v3/<int:score>")
def success_v3(score):
    if score >= 90:
        res = "Excellent!"
    else:
        res = "Keep trying!"
    exp = {'score': score, 'result': res}

    return render_template("result_v3.html", result = exp)


# If statement now. Now it's the template including the if else statement, not the function. This allows us to keep our logic in the template and makes it easier to manage the presentation of our data.
@app.route("/success_v4/<int:score>")
def success_v4(score):
    return render_template("result_v4.html", score = score)


"""
What if we want to direct the user to different routes based on some parameters, like score? We can use the url_for function to generate URLs dynamically based on the parameters passed to the function. 
This allows us to create more flexible and dynamic applications that can adapt to different user inputs and conditions.
"""

# From a form submission, we can calculate the total score and then redirect the user to a different route based on the score. 
# For example, if the total score is greater than or equal to 90, we can redirect the user to the success_v4 route with the score as a parameter. 
# If the total score is less than 90, we can redirect the user to a different route that shows a message encouraging them to keep trying

# Route for failed score
@app.route("/failed/<int:score>")
def failed(score):
    return render_template("failed.html", score = score)


@app.route("/get_results", methods = ["GET", "POST"])
def get_results():
    total_score = 0
    # POST: we get the form data, calculate the total score
    if request.method == "POST":
        science = float(request.form.get("science", 0))
        maths = float(request.form.get("maths", 0))
        c = float(request.form.get("c", 0))
        datascience = float(request.form.get("datascience", 0))
        total_score = (science + maths + c + datascience) / 4
    # GET: we just render the form to get the results
    else:
        return render_template("get_results.html")
    # Redirect the user to the appropriate route based on the total score
    return redirect(url_for("success_v4", score = total_score)) if total_score >= 90 else redirect(url_for("failed", score = total_score))


if __name__ == "__main__":
    app.run(debug=True)