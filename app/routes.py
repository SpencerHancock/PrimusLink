from app import app
from flask import render_template, redirect, flash
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
	user = {"username":"spencer"}
	return render_template("index.html")

@app.route("/home")
def home():
	user = {"username":"spencer"}
	users = [
		{"username":"bill","description" : "I am a strong, burly gay man"},
		{"username":"carol","description" : "I am a forty year old woman looking for my first man"}

		 	]
	return render_template("homepage.html", user=user, users=users)

@app.route("/login", methods=["POST", "GET"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash("{} tried to login with {} password".format(form.username.data, form.password.data))
		return redirect("/home")
	return render_template("login.html", form=form)

