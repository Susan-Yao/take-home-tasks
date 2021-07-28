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
        url = 'http://127.0.0.1:5000/menu_review/get_all_menu_reviews'
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    # ------------------ create ------------------
    def test_A1_01(self):
        url = 'http://127.0.0.1:5000/menu/add_new_menu'
        parameters = {"name": "menu 3",
                    "start": "2021-08-02",
                    "end": "2021-08-08"}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    # ------------------ read ------------------
    def test_A2_01(self):
        url = 'http://127.0.0.1:5000/menu_review/add_new_menu_review'
        parameters = {"menu_id":10,
                    "user_id":20,
                    "rating":5,
                    "comment":"Good!!"}
        response = self.app.get(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    # ------------------ update ------------------
    def test_A3_01(self):
        url = 'http://127.0.0.1:5000/menu_review/update_menu_review_details'
        parameters = {"menu_review_id":30,
                    "rating":5,
                    "comment":"Good updated!"}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    # ------------------ delete ------------------
    def test_A4_02(self):
        url = 'http://127.0.0.1:5000/menu_review/delete_menu_review'
        parameters = {"menu_review_id": 100}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)