import os

path = 'sqlite:///' + os.path.abspath(os.path.dirname(__name__))

class Config(object):
	SECRET_KEY = "hello my name is secret key"
	SQLALCHEMY_DATABASE_URI = os.path.join(path,"todo.db")
	SQLALCHEMY_TRACK_MODIFICATIONS = False