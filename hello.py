from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField # Stringfield - input field or box, SubmitField - submit button
from wtforms.validators import DataRequired # DataRequired - Validating field entries
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create a flask instance
app = Flask(__name__)
# Create a database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_web.db' # Using SQLite Database 
# Format app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql//username:password@localhost/db_name' # Using SQLite Database

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:PaSs_KyCx_1234@localhost/user_data' # Using MySQL Database
# Secret key
app.config['SECRET_KEY'] = "P@ssw0rd_123" # For CSRF protection in WTForm

# Initialize database
db = SQLAlchemy(app)

# Create a model 
class User(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.name}>'  # Changed %r to f-string

# Create the Flask application context
with app.app_context():
    # Call db.create_all() and any other database operations here
    db.create_all()

# Create a flask form Class for Users
class UserForm(FlaskForm):
    name = StringField("Name", validators = [DataRequired()])
    email = StringField("Email", validators = [DataRequired()])
    submit = SubmitField("Submit")

# Create a flask form Class
class NamerForm(FlaskForm):
    name = StringField("What is your name?", validators = [DataRequired()])
    submit = SubmitField("Submit")

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

@app.route('/users/add', methods = ['GET', 'POST'])
def add_user():
    name = None
    add_user_form = UserForm()
    
    if add_user_form.validate_on_submit():
        user = User.query.filter_by(email=add_user_form.email.data).first()
        if user is None:
            user = User(name=add_user_form.name.data, email=add_user_form.email.data)
            db.session.add(user)
            db.session.commit()
        name = add_user_form.name.data
        add_user_form.name.data = ''
        add_user_form.email.data = ''
        flash("A user was added in the database!")
    user_data = User.query.order_by(User.date_added)
    
    return render_template("add_user.html", form=add_user_form, name=name, user_data=user_data)

    

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
    
# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Forms
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form submitted successfully!")
        
    return render_template("name.html", name=name, form=form)
