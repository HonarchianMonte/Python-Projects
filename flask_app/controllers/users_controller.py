from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe

bcrypt = Bcrypt(app)
# bcrypt.generate_password_hash(password_string)
# bcrypt.check_password_hash(hashed_password, password_string)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recipes') #taking us from home page to recipe dashboard
def welcome():
    if not "user_id" in session:
        return redirect('/')
    data = {
        "id": session["user_id"]
    }
    user_logged_in = User.get_by_id(data)
    recipes = Recipe.recipe_dashboard()
    return render_template('welcome.html', user = user_logged_in, recipes_list = recipes)

@app.route("/submit/user", methods=['POST'])
def register():
    if not User.validate(request.form):
        return  redirect('/')
    hashed_pw =bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password' : hashed_pw
    }
    session['user_id'] = User.create_user(data)
    return redirect ('/recipes')


@app.route ("/users/logout")
def logout():
    del session['user_id']
    return redirect('/')

#Login
@app.route("/users/login", methods=['POST'])
def login():
    data = {
        "email": request.form["email"]
    }
    user_from_db = User.get_by_email(data)
    if not user_from_db:
        print("didn't find user")
        flash("Invalid Credentials", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
        flash("Invalid Credentials", "login")
        print("password failed")
        return redirect("/")
    session['user_id'] = user_from_db.id
    print("login post successful")
    return redirect('/recipes')


