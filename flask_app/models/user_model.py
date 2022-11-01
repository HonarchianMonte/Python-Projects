from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        return connectToMySQL(DATABASE).query_db(query,data)
        
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate(registered_data):
        is_valid = True
        if len(registered_data['first_name']) <2:
            flash(" First Name - letters only, at least 2 characters needed" , "reg")
            is_valid = False
        if len(registered_data['last_name']) <2:
            flash("Last Name - letters only, at least 2 characters needed", "reg")
            is_valid = False
        if len(registered_data['email']) <1:
                flash("Please provide email", "reg",)
                is_valid = False
        if not EMAIL_REGEX.match(registered_data['email']):
            is_valid = False
            flash("invalid email", "reg")
        potential_user = User.get_by_email(registered_data)
        if potential_user: #if we have a user, don't let them register with this email!
                is_valid = False
                flash("Email already in DB, hope it's you...", "reg")
        if len(registered_data['password']) < 8:
                flash("Password must be at least 8 chars", "reg")
                is_valid = False
        if not registered_data['password'] == registered_data['confirm_password']:
                flash("Passwords don't match", "reg")
                is_valid = False
        return is_valid