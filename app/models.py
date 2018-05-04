from datetime import datetime
from app import db

class ToDo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(200))
	timestamp = db.Column(db.DateTime, default=datetime.now)
	complete = db.Column(db.Boolean, default=False)