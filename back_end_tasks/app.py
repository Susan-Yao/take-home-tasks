from functools import wraps
import os
from flask import Flask, request, jsonify, json
from flask_cors import *

# peewee database
from peewee import Database, PostgresqlDatabase

app = Flask(__name__)

CORS(app, supports_credentials=True)

# get db connection details from environment variables
db_name = os.environ.get("DB_NAME")
user_name = os.environ.get("USER_NAME")
port_num = os.environ.get("PORT_NUM")
db_pw = os.environ.get("DB_PW")

db = PostgresqlDatabase(db_name, host='localhost', port=port_num, user=user_name, password=db_pw)

from user_module import user_bp
from menu_module import menu_bp
from recipe_module import recipe_bp
from menu_review_module import menu_review_bp
from recipe_review_module import recipe_review_bp
from menu_recipe_module import menu_recipe_bp

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(menu_bp, url_prefix='/menu')
app.register_blueprint(recipe_bp, url_prefix='/recipe')
app.register_blueprint(menu_review_bp, url_prefix='/menu_review')
app.register_blueprint(recipe_review_bp, url_prefix='/recipe_review')
app.register_blueprint(menu_recipe_bp, url_prefix='/menu_recipe')

# API token
# Can be used by add "@token_required" under each API
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'API-TOKEN' in request.headers:
            token = request.headers['API-TOKEN']
        if not token:
            return jsonify(error = 'Token is missing!')
        print('TOKEN is: {}'.format(token))
        return f(*args, **kwargs)
    return decorated

@app.route('/')
@token_required
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
