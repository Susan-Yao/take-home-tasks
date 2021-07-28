from unittest import TestCase
import unittest

import os
from flask import request, json

from app import app
from models import db

class Test_Menu(TestCase):

    @classmethod
    def setUpClass(self): # executed before each test
        print('### Testing Menu Module ... ###')
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yyxx@localhost/HelloFresh'
        app.config['SECRET_KEY'] = "random string"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
        self.app = app.test_client()

    # ------------------ create ------------------
    def test_A1_01(self):
        url = 'http://127.0.0.1:5000/menu_recipe/add_new_menu_recipe'
        parameters = {"menu_id": 10,
                    "recipe_id": 5}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    # ------------------ read ------------------
    def test_A2_01(self):
        url = 'http://127.0.0.1:5000/menu_recipe/get_menu_recipe_details'
        parameters = {"menu_id": 100}
        response = self.app.get(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    # ------------------ delete ------------------
    def test_A4_02(self):
        url = 'http://127.0.0.1:5000/menu_recipe/delete_menu_recipe'
        parameters = {"menu_id": 100, "recipe_id": 5}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)