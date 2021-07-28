from flask import Blueprint, jsonify, request, json
from models import User, Menu
import datetime
menu_bp = Blueprint('menu', __name__) # register the blueprint

# list
@menu_bp.route('/get_all_menus', methods = ['GET'])
def get_all_menus():
    query = Menu.select()
    all_menus = []
    for q in query:
        menu = (q.menu_id, q.menuname, q.start_date, q.end_date)
        all_menus.append(menu)
    return jsonify(status = 1, result = all_menus)

# create a new menu
@menu_bp.route('/add_new_menu', methods = ['POST'])
def add_new_menu():
    data = request.get_data()
    json_data = json.loads(data)
    start_date = json_data['start']
    end_date = json_data['end']
    menu_name = json_data['name']

    menu = Menu.get_or_none(Menu.start_date == str(start_date), Menu.end_date == str(end_date))

    if menu is None: # no menu for this period
        Menu.insert(menuname = menu_name, start_date = start_date, end_date = end_date).execute()
        return jsonify(status = 1, hint = "New menu is added successfully")
    else:
        return jsonify(status = -1, error = "Menu for this period exists")

# read
@menu_bp.route('/get_menu_details', methods = ['GET'])
def get_menu_details():
    data = request.get_data()
    json_data = json.loads(data)
    menu_id = json_data['menuid']

    menu = Menu.get_or_none(Menu.menu_id == int(menu_id))

    if menu is not None: # the menu exists
        result = {}
        name = menu.menuname
        start = menu.start_date
        end = menu.end_date
        result['menu_id'] = menu_id
        result['name'] = name
        result['start'] = start.strftime('%Y-%m-%d')
        result['end'] = end.strftime('%Y-%m-%d')
        return jsonify(status = 1, result = result)
    else:
        return jsonify(status = -1, error = "This menu does not exist.")

# update
@menu_bp.route('/update_menu_details', methods = ['POST'])
def update_menu_details():
    data = request.get_data()
    json_data = json.loads(data)
    menu_id = json_data['menuid']
    name = json_data['name']
    start = json_data['start']
    end = json_data['end']

    menu = Menu.get_or_none(Menu.menu_id == int(menu_id))

    if menu is not None: # the menu exists

        if name == "":
            menu_name = menu.menuname
        else:
            menu_name = name

        if start == "":
            start_date = menu.start_date
        else:
            start_date = start

        if end == "":
            end_date = menu.end_date
        else:
            end_date = end

        query = Menu.update(menuname = menu_name, start_date = start_date, end_date = end_date).where(Menu.menu_id == int(menu_id))
        query.execute()
        return jsonify(status = 1, hint = "The menu's details is updated successfully")
    else:
        return jsonify(status = -1, error = "This menu does not exist.")

# delete
@menu_bp.route('/delete_menu', methods = ['POST'])
def delete_menu():
    data = request.get_data()
    json_data = json.loads(data)
    menu_id = json_data['menuid']

    menu = Menu.get_or_none(Menu.menu_id == int(menu_id))

    if menu is not None: # the menu exists
        menu.delete_instance()
        return jsonify(status = 1, hint = "The menu is deleted successfully")
    else:
        return jsonify(status = -1, error = "This menu does not exist.")