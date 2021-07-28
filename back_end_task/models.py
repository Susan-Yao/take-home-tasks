from peewee import *
import datetime

from app import db

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    user_id = PrimaryKeyField()
    user_name = TextField(null=False)
    user_email = TextField(null=False)

class Menu(BaseModel):
    menu_id = PrimaryKeyField()
    menuname = TextField(null=False)
    start_date = DateField(null=False)
    end_date = DateField(null=False)

class Recipe(BaseModel):
    recipe_id = PrimaryKeyField()
    title = TextField(null=False)
    subtitle = TextField()
    introduction = TextField()
    allergens = TextField()
    preparation_time = TextField()
    utensils = TextField()
    difficulty = TextField()
    classification = TextField()
    ingredients = TextField()
    instructions = TextField()
    nutrition = TextField()
    photo = TextField()

# M-M relationship
class Menu_Recipe(BaseModel):
    menu_id = ForeignKeyField(Menu)
    recipe_id = ForeignKeyField(Recipe)

class Recipe_Review(BaseModel):
    recipe_review_id = PrimaryKeyField()
    recipe_id = ForeignKeyField(Recipe)
    rating = IntegerField()
    comment = TextField()
    user_id = ForeignKeyField(User)

class Menu_Review(BaseModel):
    id = PrimaryKeyField()
    menu_id = ForeignKeyField(Menu)
    rating = IntegerField()
    comment = TextField()
    user_id = ForeignKeyField(User)

db.connect()
db.create_tables([User, Menu, Menu_Review, Recipe, Menu_Recipe, Recipe_Review])