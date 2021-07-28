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
        url = 'http://127.0.0.1:5000/recipe_review/get_all_recipe_reviews'
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    # ------------------ create ------------------
    def test_A1_01(self):
        url = 'http://127.0.0.1:5000/recipe_review/add_new_recipe_review'
        parameters = {"recipe_id":100,
                    "user_id":2,
                    "rating":5,
                    "comment":"Good!!"}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    # ------------------ read ------------------
    def test_A2_01(self):
        url = 'http://127.0.0.1:5000/recipe_review/get_recipe_review_details'
        parameters = {"recipe_review_id": 300}
        response = self.app.get(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    # ------------------ update ------------------
    def test_A3_01(self):
        url = 'http://127.0.0.1:5000/recipe_review/update_recipe_review_details'
        parameters = {"recipe_review_id": 300,
                    "rating": 5,
                    "comment": "Nice~!"}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    # ------------------ delete ------------------
    def test_A4_02(self):
        url = 'http://127.0.0.1:5000/recipe_review/delete_recipe_review'
        parameters = {"recipe_review_id": 30}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)