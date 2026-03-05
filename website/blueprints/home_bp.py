from flask import Blueprint, render_template
from flask import Blueprint, render_template, request

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def home():
    # renderowany jest szablon html z formularzem ( folder templates)
    return render_template('formularz.html')
