from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import ToDo


@app.route("/", methods=["GET","POST"])
def index():
	list_all = ToDo.query.all()
	return render_template("index.html", list=list_all)

@app.route("/add", methods=["POST"])
def add():
	txt = request.form.get("todoitem")	
	if txt is not None:
		new_element = ToDo(text=txt)
		db.session.add(new_element)
		db.session.commit()
	return redirect(url_for("index"))

@app.route("/update", methods=["POST"])
def update():
	list_all = ToDo.query.all()
	for item in list_all:
		if request.form.get(str(item.id)) is not None:
			element = ToDo.query.filter_by(id=int(item.id)).first()
			if  element is not None:
				element.complete = True
				db.session.commit()
	return redirect(url_for("index"))