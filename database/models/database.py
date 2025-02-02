from peewee import Model, CharField
from database.data import db

class Livros(Model):
    name_book = CharField()
    name_author= CharField()

    class Meta:
        database = db