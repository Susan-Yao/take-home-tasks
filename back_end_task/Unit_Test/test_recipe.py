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

    # ------------------ list ------------------
    def test_A0_01(self):
        url = 'http://127.0.0.1:5000/recipe/get_all_recipes'
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    # ------------------ create ------------------
    def test_A1_01(self): # can be added
        url = 'http://127.0.0.1:5000/recipe/add_new_recipe'
        parameters = {"title":"new recipe RRRR",
                    "subtitle": "",
                    "intro":"",
                    "allergen":"",
                    "time":"",
                    "diff":"",
                    "uten":"",
                    "class":"",
                    "photo":"",
                    "ingre":"",
                    "instru":"",
                    "nutri":""}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    # ------------------ read ------------------
    def test_A2_01(self): # can be read
        url = 'http://127.0.0.1:5000/recipe/get_recipe_details'
        parameters = {"recipeid": 1}
        response = self.app.get(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    def test_A2_02(self): # can not be read
        url = 'http://127.0.0.1:5000/recipe/get_recipe_details'
        parameters = {"recipeid": 100}
        response = self.app.get(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    # ------------------ update ------------------
    def test_A3_01(self): # can be updated
        url = 'http://127.0.0.1:5000/recipe/update_recipe_details'
        parameters = {"recipeid":1,
                    "title":"new recipe updated",
                    "subtitle": "",
                    "intro":"",
                    "allergen":"",
                    "time":"",
                    "diff":"",
                    "uten":"",
                    "class":"",
                    "photo":"",
                    "ingre":"",
                    "instru":"",
                    "nutri":""}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    def test_A3_02(self): # can not be updated
        url = 'http://127.0.0.1:5000/recipe/update_recipe_details'
        parameters = {"recipeid":100,
                    "title":"new recipe updated",
                    "subtitle": "",
                    "intro":"",
                    "allergen":"",
                    "time":"",
                    "diff":"",
                    "uten":"",
                    "class":"",
                    "photo":"",
                    "ingre":"",
                    "instru":"",
                    "nutri":""}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    # ------------------ delete ------------------
    def test_A4_01(self): # can be deleted
        url = 'http://127.0.0.1:5000/recipe/delete_recipe'
        parameters = {"recipeid":1}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    def test_A4_02(self): # cannot be deleted
        url = 'http://127.0.0.1:5000/recipe/delete_recipe'
        parameters = {"recipeid":2}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)