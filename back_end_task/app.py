from functools import wraps

from flask import Flask, request, jsonify, json
from flask_cors import *
from flask_restplus import Api

# peewee database
from peewee import Database, PostgresqlDatabase

app = Flask(__name__)

CORS(app, supports_credentials=True)

db = PostgresqlDatabase('HelloFresh', host='localhost', port=5432, user='postgres', password='yyxx')

from user_module import user_bp
from menu_module import menu_bp
from recipe_module import recipe_bp
from menu_review_module import menu_review_bp
from recipe_review_module import recipe_review_bp
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(menu_bp, url_prefix='/menu')
app.register_blueprint(recipe_bp, url_prefix='/recipe')
app.register_blueprint(menu_review_bp, url_prefix='/menu_review')
app.register_blueprint(recipe_review_bp, url_prefix='/recipe_review')

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
def hello_world():
    return 'Hello World!'

@app.route('/get_all_recipes', methods = ['GET'])
# @token_required
def get_all_recipes():
    return 'get_all_recipes!'


if __name__ == '__main__':
    app.run()
