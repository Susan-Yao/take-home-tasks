from flask import Blueprint, jsonify, request, json
from models import User
user_bp = Blueprint('user', __name__) # register the blueprint

# list
@user_bp.route('/get_all_users', methods = ['GET'])
def get_all_users():
    query = User.select(User.user_id, User.user_name, User.user_email)
    all_users = []
    for q in query:
        user = (q.user_id, q.user_name, q.user_email)
        all_users.append(user)
    return jsonify(status = 1, result = all_users)

# create
@user_bp.route('/add_new_user', methods = ['POST'])
def add_a_new_user():
    data = request.get_data()
    json_data = json.loads(data)
    email = json_data['email']
    name = json_data['name']

    query = User.select(User.user_email)
    all_emails = []
    for q in query:
        all_emails.append(q.user_email)
    if email not in all_emails:
        User.insert(user_name = name, user_email = email).execute()
        return jsonify(status = 1, hint = "New user is added successfully.")
    else:
        return jsonify(status = -1, error = "This user already exists.")

# read
@user_bp.route('/get_user_details', methods = ['GET'])
def get_user_details():
    data = request.get_data()
    json_data = json.loads(data)
    user_id = json_data['userid']

    user = User.get_or_none(User.user_id == int(user_id))

    if user is not None: # the user exists
        result = {}
        name = user.user_name
        email = user.user_email
        result['user_id'] = user_id
        result['name'] = name
        result['email'] = email
        return jsonify(status = 1, result = result)
    else:
        return jsonify(status = -1, error = "This user does not exist.")

# update
@user_bp.route('/update_user_details', methods = ['POST'])
def update_user_details():
    data = request.get_data()
    json_data = json.loads(data)
    user_id = json_data['userid']
    name = json_data['name']

    user = User.get_or_none(User.user_id == int(user_id))

    if user is not None: # the user exists
        query = User.update(user_name = name).where(User.user_id == int(user_id))
        query.execute()
        return jsonify(status = 1, hint = "The user's details is updated successfully")
    else:
        return jsonify(status = -1, error = "This user does not exist.")

# delete
@user_bp.route('/delete_user', methods = ['POST'])
def delete_user():
    data = request.get_data()
    json_data = json.loads(data)
    user_id = json_data['userid']

    user = User.get_or_none(User.user_id == int(user_id))

    if user is not None: # the user exists
        user.delete_instance()
        return jsonify(status = 1, hint = "The user is deleted successfully")
    else:
        return jsonify(status = -1, error = "This user does not exist.")