from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User

@app.route('/recipes/new')
def create():
    return render_template('new_recipe.html')

@app.route("/submit/recipe", methods=['POST'])
def new_recipe():
    data = {
    "user_id": session["user_id"],
    "name": request.form["name"],
    "under_30_mins": request.form["under_30_mins"],
    "description": request.form["description"],
    "instructions": request.form["instructions"],
    "cooked_date": request.form["cooked_date"]
    }
    if not Recipe.validate(data):  #validate from the class, then return to it's failed location.
        return redirect('/recipes/new')
    Recipe.create_recipe(data)
    return redirect ('/recipes')


    #Delete
@app.route('/recipe/delete/<int:id>')
def delete(id):
    data ={
        'id':id
    }
    Recipe.delete(data)
    return redirect('/recipes')

#EDIT/Update
@app.route('/recipe/update', methods=['POST']) #Action route for updates
def update():
    data ={
    "id": request.form["id"],
    "name": request.form["name"],
    "under_30_mins": request.form["under_30_mins"],
    "description": request.form["description"],
    "instructions": request.form["instructions"],
    "cooked_date": request.form["cooked_date"]
    }
    if not Recipe.validate(data):
        return redirect(f"/recipe/edit/{data['id']}")
    Recipe.update(request.form)
    return redirect("/recipes")

@app.route('/recipe/edit/<int:id>') # this is the creation of the variable <int:id>
def edit(id):
    data ={
        "id":id
    }
    return render_template("edit_recipe.html", recipe=Recipe.show_one_recipe(data))

#SHOW
@app.route('/recipe/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    data1 = {
        "id": session['user_id']
    }
    this_user = User.get_by_id(data1)
    return render_template("show_recipe.html", recipe=Recipe.show_one_recipe(data), user = this_user )