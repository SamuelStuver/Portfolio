import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from portfolio import app, db
#from portfolio.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
#from portfolio.models import User, Post
#from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/career_summary")
def career_summary():
    return render_template('home.html')

@app.route("/skills")
def skills():
    return render_template('home.html')

@app.route("/experience")
def experience():
    return render_template('home.html')

@app.route("/education")
def education():
    return render_template('home.html')
