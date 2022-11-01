from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Recipe:
    def __init__(self,data):
        self.user_id = data['user_id'] # needed for edit/ delete for specific user.
        self.id = data['id']
        self.name = data ['name']
        self.under_30_mins = data ['under_30_mins']
        self.description = data['description']
        self.instructions = data['instructions']
        self.cooked_date = data['cooked_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#create recipe
    @classmethod
    def create_recipe(cls,data):
        query = "INSERT INTO recipes (user_id, name, under_30_mins, description, instructions, cooked_date) VALUES (%(user_id)s,%(name)s, %(under_30_mins)s, %(description)s, %(instructions)s, %(cooked_date)s)"
        return connectToMySQL(DATABASE).query_db(query,data)

#all recipes
    @classmethod
    def recipe_dashboard(cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id"
        results = connectToMySQL(DATABASE).query_db(query)
        all_recipes = []
        for row_from_db in results:
            recipe_instance = cls(row_from_db)
            data = { #needs all data
                "id": row_from_db["users.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "email": row_from_db["email"],
                "password": row_from_db["password"],
                "created_at": row_from_db["users.created_at"],
                "updated_at": row_from_db["users.updated_at"]
            }
            this_user = user_model.User(data)
            recipe_instance.posted_by = this_user #posted_by is made up right here.
            all_recipes.append(recipe_instance)
        return all_recipes

#show one
    @classmethod
    def show_one_recipe(cls,data):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        this_recipe = cls(results[0])
        for row_from_db in results:
            data = {
                "id": row_from_db["users.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "email": row_from_db["email"],
                "password": row_from_db["password"],
                "created_at": row_from_db["users.created_at"],
                "updated_at": row_from_db["users.updated_at"]
            }
            this_user = user_model.User(data)
            this_recipe.posted_by = this_user
        return this_recipe


    @staticmethod
    def validate(recipe_data):
        is_valid = True
        if len(recipe_data['name']) <3:
            flash("Recipe Name, at least 3 characters needed", "new_recipe")
            is_valid = False
        if len(recipe_data['description']) <3:
            flash("Description, at least 3 characters needed", "new_recipe")
            is_valid = False
        if len(recipe_data['instructions']) <3:
            flash("Instructions, at least 3 characters needed", "new_recipe")
            is_valid = False
        if not (recipe_data['cooked_date']):
            flash("Date must not be blank", "new_recipe")
            is_valid = False    
        return is_valid


    #DELETE
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    #(EDIT/UPDATE)
    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name=%(name)s, cooked_date=%(cooked_date)s, instructions=%(instructions)s, under_30_mins = %(under_30_mins)s, description = %(description)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
