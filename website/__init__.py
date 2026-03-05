from flask import Flask
import os

from website.blueprints.home_bp import home_bp
from website.blueprints.mapa_bp import mapa_bp


def create_app():
    #tworzona jest aplikacja flask,
    app = Flask(__name__)

    # rejestracja blueprint w celu obslugi poszczegolnych adresow url

    # pierwszy - czyli to co sie dzieje po wejściu na stronę - u nas formularz
    app.register_blueprint(home_bp)

    # drugi - po wysłaniu formularza - generowanie mapy
    app.register_blueprint(mapa_bp)

    return app
