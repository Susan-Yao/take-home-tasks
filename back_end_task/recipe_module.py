from flask import Blueprint, jsonify, request, json
from models import User, Menu, Recipe
import datetime
recipe_bp = Blueprint('recipe', __name__) # register the blueprint

# list
@recipe_bp.route('/get_all_recipes', methods = ['GET'])
def get_all_recipes():
    query = Recipe.select()
    all_recipes = []
    for q in query:
        recipe = (q.title, q.subtitle, q.introduction, q.allergens, q.preparation_time, q.utensils,
                  q.difficulty, q.classification, q.photo, q.ingredients, q.instructions, q.nutrition)
        all_recipes.append(recipe)
    return jsonify(status = 1, result = all_recipes)

# create a new recipe
@recipe_bp.route('/add_new_recipe', methods = ['POST'])
def add_new_menu():
    data = request.get_data()
    json_data = json.loads(data)

    title = json_data['title']
    subtitle = json_data['subtitle']
    intro = json_data['intro']
    allergen = json_data['allergen']
    time = json_data['time']
    diff = json_data['diff']
    utensil = json_data['uten']
    classification = json_data['class']
    photo = json_data['photo']

    ingredient = json_data['ingre']
    instruction = json_data['instru']
    nutrition = json_data['nutri']


    recipe = Recipe.get_or_none(Recipe.title == str(title))

    if recipe is None: # the recipe does not exist --- can add
        Recipe.insert(title = title, subtitle = subtitle, introduction = intro, allergens = allergen,
                      preparation_time = time, difficulty = diff, utensils = utensil,
                      classification = classification, photo = photo, nutrition = nutrition,
                      ingredients = ingredient, instructions = instruction).execute()
        return jsonify(status = 1, hint = "New recipe is added successfully")
    else:
        return jsonify(status = -1, error = "The recipe already exists")

# read
@recipe_bp.route('/get_recipe_details', methods = ['GET'])
def get_recipe_details():
    data = request.get_data()
    json_data = json.loads(data)
    recipe_id = json_data['recipeid']

    recipe = Recipe.get_or_none(Recipe.recipe_id == int(recipe_id))

    if recipe is not None: # the recipe exists
        result = {}
        result['title'] = recipe.title
        result['subtitle'] = recipe.subtitle
        result['intro'] = recipe.introduction
        result['allergen'] = recipe.allergens
        result['time'] = recipe.preparation_time
        result['uten'] = recipe.utensils
        result['difficulty'] = recipe.difficulty
        result['class'] = recipe.classification
        result['ingredient'] = recipe.ingredients
        result['nutrition'] = recipe.nutrition
        result['instruction'] = recipe.instructions
        result['photo'] = recipe.photo
        return jsonify(status = 1, result = result)
    else:
        return jsonify(status = -1, error = "This menu does not exist.")

# update
@recipe_bp.route('/update_recipe_details', methods = ['POST'])
def update_recipe_details():
    data = request.get_data()
    json_data = json.loads(data)
    recipe_id = json_data['recipeid']
    title = json_data['title']
    subtitle = json_data['subtitle']
    intro = json_data['intro']
    allergen = json_data['allergen']
    time = json_data['time']
    utensil = json_data['uten']
    diff = json_data['diff']
    classification = json_data['class']
    ingre = json_data['ingre']
    nutri = json_data['nutri']
    instru = json_data['instru']
    photo = json_data['photo']

    recipe = Recipe.get_or_none(Recipe.recipe_id == int(recipe_id))

    if recipe is not None: # the recipe exists
        query = Recipe.update(title = title, subtitle = subtitle, introduction = intro,
                            allergens = allergen, preparation_time = time, utensils = utensil,
                            difficulty = diff, classification = classification, photo = photo,
                            ingredients = ingre, instructions = instru, nutrition = nutri).where(Recipe.recipe_id == int(recipe_id))
        query.execute()
        return jsonify(status = 1, hint = "The recipe's details is updated successfully")
    else:
        return jsonify(status = -1, error = "This recipe does not exist.")

# delete
@recipe_bp.route('/delete_recipe', methods = ['POST'])
def delete_recipe():
    data = request.get_data()
    json_data = json.loads(data)
    recipe_id = json_data['recipeid']

    recipe = Recipe.get_or_none(Recipe.recipe_id == int(recipe_id))

    if recipe is not None: # the menu exists
        recipe.delete_instance()
        return jsonify(status = 1, hint = "The recipe is deleted successfully")
    else:
        return jsonify(status = -1, error = "This recipe does not exist.")