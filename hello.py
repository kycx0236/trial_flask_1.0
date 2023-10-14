from flask import Flask, render_template

# Create a flask instance
app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)

"""
Other filters:
safe - allow html tags to be invoke
capitalize - capitalize 
lower - lowercase
upper - upper case
title - "Capitalize the first letter of a string"
trim - remove trailing spaces in the end
striptags - Remove html tags

Using these {{ variable_name|filter }} is for variables
Using these {% if statements or for loop %} is for for loops and if statements or logic statements

"""

# Create a flask director or route (URL)
@app.route('/')

#def index():
#   return "<h1>Hello World!</h1>"
def index():
    first_name = "kurt"
    text = "This is a <strong>TRIAL</strong> html page using Flask and Jinja."
    fav_char = ["Gojo", "Itadori", "Megumi"]
    
    return render_template("index.html", f_name=first_name, stuffs = text, fav_char = fav_char)

# localhost:5000/user/Kurt
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

#def user(name):
#    return "<h1>Hello {}!</h1>".format(name)

# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)

def invalid_url(e):
    return render_template("404.html"), 404

# Internal Error Pages
def internal_error_url(e):
    return render_template("500.html"), 500
    