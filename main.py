from flask import Flask, url_for, render_template, make_response, Blueprint
from flask import send_from_directory, flash, request, redirect
from flask_login import *
from utils import *
import os
from pathlib import Path

from database import db_create as db

main_1 = Blueprint('main',__name__)

@main_1.route('/')
def index():
    return render_template('index.html')


@main_1.route('/profile')
def profile():
    return render_template('profile.html')

