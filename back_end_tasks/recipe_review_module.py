from flask import Blueprint, jsonify, request, json
from models import User, Menu, Recipe_Review, Recipe
import datetime
recipe_review_bp = Blueprint('recipe_review', __name__) # register the blueprint

# list
@recipe_review_bp.route('/get_all_recipe_reviews', methods = ['GET'])
def get_all_recipe_reviews():
    query = Recipe_Review.select()
    all_recipe_reviews = []
    for q in query:
        recipe_review = {}
        recipe_review['recipe_id'] = q.recipe_id.recipe_id
        recipe_review['user_id'] = q.user_id.user_id
        recipe_review['rating'] = q.rating
        recipe_review['comment'] = q.comment
        all_recipe_reviews.append(recipe_review)
    return jsonify(status = 1, result = all_recipe_reviews)

# create a new menu review
@recipe_review_bp.route('/add_new_recipe_review', methods = ['POST'])
def add_new_recipe_review():
    data = request.get_data()
    json_data = json.loads(data)
    recipe_id = json_data['recipe_id']
    user_id = json_data['user_id']
    rating = json_data['rating']
    comment = json_data['comment']

    recipe_review = Recipe_Review.get_or_none(Recipe_Review.recipe_id == str(recipe_id), Recipe_Review.user_id == str(user_id))
    recipe = Recipe.get_or_none(Recipe.recipe_id == int(recipe_id))

    if recipe_review is None: # the user has not made a menu review for the menu
        if recipe is None:
            return jsonify(status=-1, error="The recipe does not exist")
        else:
            Recipe_Review.insert(recipe_id = recipe_id, user_id = user_id, rating = rating, comment = comment).execute()
            return jsonify(status = 1, hint = "New recipe review is added successfully")
    else:
        return jsonify(status = -1, error = "The user has already made a recipe review for this recipe")

# read
@recipe_review_bp.route('/get_recipe_review_details', methods = ['GET'])
def get_recipe_review_details():
    data = request.get_data()
    json_data = json.loads(data)
    menu_review_id = json_data['recipe_review_id']

    menu_review = Recipe_Review.get_or_none(Recipe_Review.recipe_review_id == int(menu_review_id))

    if menu_review is not None: # the menu review exists
        result = {}
        result['menu_review_id'] = menu_review_id
        result['user_id'] = menu_review.user_id.user_id
        result['comment'] = menu_review.comment
        result['rating'] = menu_review.rating
        return jsonify(status = 1, result = result)
    else:
        return jsonify(status = -1, error = "This recipe review does not exist.")

# update
@recipe_review_bp.route('/update_recipe_review_details', methods = ['POST'])
def update_recipe_review_details():
    data = request.get_data()
    json_data = json.loads(data)
    menu_review_id = json_data['recipe_review_id']
    rating = json_data['rating']
    comment = json_data['comment']

    menu_review = Recipe_Review.get_or_none(Recipe_Review.recipe_review_id == int(menu_review_id))

    if menu_review is not None: # the recipe review exists
        query = Recipe_Review.update(comment = comment, rating = rating).where(Recipe_Review.recipe_review_id == int(menu_review_id))
        query.execute()
        return jsonify(status = 1, hint = "The recipe review is updated successfully")
    else:
        return jsonify(status = -1, error = "This recipe review does not exist.")

# delete
@recipe_review_bp.route('/delete_recipe_review', methods = ['POST'])
def delete_recipe_review():
    data = request.get_data()
    json_data = json.loads(data)
    menu_review_id = json_data['recipe_review_id']

    menu_review = Recipe_Review.get_or_none(Recipe_Review.recipe_review_id == int(menu_review_id))

    if menu_review is not None: # the menu review exists
        menu_review.delete_instance()
        return jsonify(status = 1, hint = "The recipe review is deleted successfully")
    else:
        return jsonify(status = -1, error = "This recipe review does not exist.")