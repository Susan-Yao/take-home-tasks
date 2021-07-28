from app import token_required # can be used by add "@token_required" under each API
from flask import Blueprint, jsonify, request, json
from models import User, Menu, Menu_Review, Recipe_Review, Menu_Recipe, Recipe
import datetime
menu_recipe_bp = Blueprint('menu_recipe', __name__) # register the blueprint

# assign recipes to a menu
@menu_recipe_bp.route('/add_new_menu_recipe', methods = ['POST'])
def add_new_menu_recipe():
    data = request.get_data()
    json_data = json.loads(data)
    menu_id = json_data['menu_id']
    recipe_id = json_data['recipe_id']

    menu_recipe = Menu_Recipe.get_or_none(Menu_Recipe.menu_id == str(menu_id), Menu_Recipe.recipe_id == str(recipe_id))
    menu = Menu.get_or_none(Menu.menu_id == int(menu_id))
    recipe = Recipe.get_or_none(Recipe.recipe_id == int(recipe_id))

    if menu_recipe is None:
        if menu is None:
            return jsonify(status=-1, error="The menu does not exist")
        if recipe is None :
            return jsonify(status=-1, error="The recipe does not exist")
        Menu_Recipe.insert(menu_id=menu_id, recipe_id=recipe_id).execute()
        return jsonify(status = 1, hint = "New menu-recipe is added successfully")
    else:
        return jsonify(status = -1, error = "The menu-recipe already exists")

# read all recipes of a menu
@menu_recipe_bp.route('/get_menu_recipe_details', methods = ['GET'])
def get_menu_recipe_details():
    data = request.get_data()
    json_data = json.loads(data)
    menu_id = json_data['menu_id']

    menu = Menu.get_or_none(Menu.menu_id == int(menu_id))

    if menu is not None: # the menu exists
        result = []
        for m in Menu_Recipe.select().where(Menu_Recipe.menu_id == int(menu_id)):
            result.append(m.recipe_id.recipe_id)
        return jsonify(status = 1, result = result)
    else:
        return jsonify(status = -1, error = "This menu review does not exist.")

# delete a recipe of a menu
@menu_recipe_bp.route('/delete_menu_recipe', methods = ['POST'])
def delete_menu_recipe():
    data = request.get_data()
    json_data = json.loads(data)
    menu_id = json_data['menu_id']
    recipe_id = json_data['recipe_id']

    menu_recipe = Menu_Recipe.get_or_none(Menu_Recipe.menu_id == int(menu_id), Menu_Recipe.recipe_id == int(recipe_id))
    menu = Menu.get_or_none(Menu.menu_id == int(menu_id))
    recipe = Recipe.get_or_none(Recipe.recipe_id == int(recipe_id))

    if menu is None:
        return jsonify(status=-1, error="This menu does not exist.")
    if recipe is None:
        return jsonify(status=-1, error="This recipe does not exist.")

    if menu_recipe is not None: # the menu-recipe exists
        menu_recipe.delete_instance()
        return jsonify(status = 1, hint = "The menu recipe is deleted successfully")
    else:
        return jsonify(status = -1, error = "This menu recipe does not exist.")