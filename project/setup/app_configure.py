from flask import Flask

from project.setup.db_init import db
from project.setup.api_init import api
from project.view.main.directors import directors_ns
from project.view.main.genres import genres_ns
from project.view.main.movies import movies_ns


def configure_app(application: Flask):
    db.init_app(application)
    api.init_app(application)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)
