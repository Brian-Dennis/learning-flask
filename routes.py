#!/usr/bin/env python3

from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User, Places
from forms import SignupForm, LoginForm, AddressForm

app = Flask(__name__)


# configuring Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/learning-flask'
db.init_app(app)


# CSRF secret key for development
app.secret_key = 'development-key'


# Index route
@app.route('/')
def index():
    return render_template("index.html")


# About route
@app.route('/about')
def about():
    return render_template("about.html")


# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if 'email' in session:
    return redirect(url_for('home'))

    form = SignupForm()

    # Validating form
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
          # Getting form data ready for submission
          newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)

          # Adding and commiting form data to db with newuser variable from above.
          db.session.add(newuser)
          db.session.commit()

          # Creating a user session redirect home
          session['email'] = newuser.email
          return redirect(url_for('home'))

    elif request.method == 'GET':
        return render_template('signup.html', form=form)


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
  if 'email' in session:
    return redirect(url_for('home'))
  form = LoginForm()

  # Validating Form
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('login.html', form=form)
    else:
      # email and password are a match
      email = form.email.data
      password = form.password.data

      # Getting the user by specified email. from db, email unique key
      user = User.query.filter_by(email=email).first()
      if user is not None and user.check_password(password):

        session['email'] = form.email.data
        return redirect(url_for('home'))
      else:
        return redirect(url_for('login'))

  elif request.method == 'GET':
      return render_template('login.html', form=form)


# Logout route
@app.route('/logout')
def logout():
  session.pop('email', None)
  return redirect(url_for('index'))


# Home route
@app.route('/home')
def home():
  if 'email' not in session:
    return redirect(url_for('login'))

  # Address Form
  form = AddressForm()

  places = []
  my_coordinates = (47.5729, 117.6822)

  # Checking form submission
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('home.html', form=form)
    else:
      # TODO: get the address
      address = form.address.data

      # TODO: query for places around it
      p = Places()
      my_coordinates = p.address_to_latlng(address)
      places = p.query(address)

      # TODO: return those results
      return render_template('home.html', form=form, my_coordinates=my_coordinates, places=places)

  elif request.method == 'GET':
    return render_template('home.html', form=form, my_coordinates=my_coordinates, places=places)

if __name__ == '__main__':
    app.run(debug=True)
