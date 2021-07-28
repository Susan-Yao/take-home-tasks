from unittest import TestCase
import unittest
from models import db
import os
from flask import request, json

import sys
sys.path.append("..")
import app

class Test_Menu(TestCase):

    @classmethod
    def setUpClass(self): # executed before each test
        print('### Testing Menu Module ... ###')
        app.config['TESTING'] = True
        app.config[
            # 'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:swen90013ec@cdb-96or1014.cd.tencentcdb.com:10146/ecoswapcup?charset=UTF8MB4'
            'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yyxx@localhost/HelloFresh'
        app.config['SECRET_KEY'] = "random string"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
        self.app = app.test_client()

    # ------------------ A-0 registration ------------------
    # customer registration, valid id (not in db), without cafeid
    def test_A0_01(self):
        url = 'http://localhost:5000/user/get_all_users'
        # parameters = {'id': 'fpQ7gU1K34T6q9QvzZ3gn3GqUlB2', 'type': '0', 'cafe': ''}
        response = self.app.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, dict(status="1"))