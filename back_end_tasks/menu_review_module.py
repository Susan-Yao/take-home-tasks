from flask import Blueprint, jsonify, request, json
from models import User, Menu, Menu_Review
import datetime
menu_review_bp = Blueprint('menu_review', __name__) # register the blueprint

# list
@menu_review_bp.route('/get_all_menu_reviews', methods = ['GET'])
def get_all_menu_reviews():
    query = Menu_Review.select()
    all_menu_reviews = []
    for q in query:
        menu_review = {}
        menu_review['menu_id'] = q.menu_id.menu_id
        menu_review['user_id'] = q.user_id.user_id
        menu_review['rating'] = q.rating
        menu_review['comment'] = q.comment
        all_menu_reviews.append(menu_review)
    return jsonify(status = 1, result = all_menu_reviews)

# create a new menu review
@menu_review_bp.route('/add_new_menu_review', methods = ['POST'])
def add_new_menu_review():
    data = request.get_data()
    json_data = json.loads(data)
    menu_id = json_data['menu_id']
    user_id = json_data['user_id']
    rating = json_data['rating']
    comment = json_data['comment']

    menu_review = Menu_Review.get_or_none(Menu_Review.menu_id == str(menu_id), Menu_Review.user_id == str(user_id))

    if menu_review is None: # the user has not made a menu review for the menu
        Menu_Review.insert(menu_id = menu_id, user_id = user_id, rating = rating, comment = comment).execute()
        return jsonify(status = 1, hint = "New menu review is added successfully")
    else:
        return jsonify(status = -1, error = "The user has already made a menu review for this menu")

# read
@menu_review_bp.route('/get_menu_review_details', methods = ['GET'])
def get_menu_review_details():
    data = request.get_data()
    json_data = json.loads(data)
    menu_review_id = json_data['menu_review_id']

    menu_review = Menu_Review.get_or_none(Menu_Review.id == int(menu_review_id))

    if menu_review is not None: # the menu review exists
        result = {}
        result['menu_review_id'] = menu_review_id
        result['user_id'] = menu_review.user_id.user_id
        result['comment'] = menu_review.comment
        result['rating'] = menu_review.rating
        return jsonify(status = 1, result = result)
    else:
        return jsonify(status = -1, error = "This menu review does not exist.")

# update
@menu_review_bp.route('/update_menu_review_details', methods = ['POST'])
def update_menu_review_details():
    data = request.get_data()
    json_data = json.loads(data)
    menu_review_id = json_data['menu_review_id']
    rating = json_data['rating']
    comment = json_data['comment']

    menu_review = Menu_Review.get_or_none(Menu_Review.id == int(menu_review_id))

    if menu_review is not None: # the menu review exists
        query = Menu_Review.update(comment = comment, rating = rating).where(Menu_Review.id == int(menu_review_id))
        query.execute()
        return jsonify(status = 1, hint = "The menu review is updated successfully")
    else:
        return jsonify(status = -1, error = "This menu review does not exist.")

# delete
@menu_review_bp.route('/delete_menu_review', methods = ['POST'])
def delete_menu_review():
    data = request.get_data()
    json_data = json.loads(data)
    menu_review_id = json_data['menu_review_id']

    menu_review = Menu_Review.get_or_none(Menu_Review.id == int(menu_review_id))

    if menu_review is not None: # the menu review exists
        menu_review.delete_instance()
        return jsonify(status = 1, hint = "The menu review is deleted successfully")
    else:
        return jsonify(status = -1, error = "This menu review does not exist.")