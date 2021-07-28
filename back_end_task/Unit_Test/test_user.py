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
        url = 'http://127.0.0.1:5000/user/get_all_users'
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    # ------------------ create ------------------
    def test_A1_01(self): # can be added
        url = 'http://127.0.0.1:5000/user/add_new_user'
        parameters = {"email":"testing-2@gmail.com", "name": "testtest"}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    def test_A1_02(self): # cannot be added
        url = 'http://127.0.0.1:5000/user/add_new_user'
        parameters = {"email": "jianjingsusan@gmail.com", "name": "Susan"}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    # ------------------ read ------------------
    def test_A2_01(self): # can be read
        url = 'http://127.0.0.1:5000/user/get_user_details'
        parameters = {"userid": 1}
        response = self.app.get(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    def test_A2_02(self): # can not be read
        url = 'http://127.0.0.1:5000/user/get_user_details'
        parameters = {"userid": 100} # no this user
        response = self.app.get(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    # ------------------ update ------------------
    def test_A3_01(self): # can be updated
        url = 'http://127.0.0.1:5000/user/update_user_details'
        parameters = {"userid": 3, "name": "Cici"}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    def test_A3_02(self): # can not be updated
        url = 'http://127.0.0.1:5000/user/update_user_details'
        parameters = {"userid": 300, "name": "Cici"}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    # ------------------ delete ------------------
    def test_A4_01(self): # can be deleted
        url = 'http://127.0.0.1:5000/user/delete_user'
        parameters = {"userid": 3}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)

    def test_A4_02(self): # cannot be deleted
        url = 'http://127.0.0.1:5000/user/delete_user'
        parameters = {"userid": 300}
        response = self.app.post(url, data = json.dumps(parameters))
        self.assertEqual(response.status_code, 200)