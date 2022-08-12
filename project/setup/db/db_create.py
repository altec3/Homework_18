from flask import Flask

from project.dao.model.director import Director
from project.dao.model.genre import Genre
from project.dao.model.movie import Movie
from project.setup.db.db_init import db
from utils import load_json, fill_db


def create_db(application: Flask) -> None:
    # Создаем базу. Добавляем таблицы в базу
    with application.app_context():
        db.drop_all()
        db.create_all()

        # Заполняем таблицы в базе
        directors_data = load_json(application.config.get("DIRECTORS_DATA"))
        genres_data = load_json(application.config.get("GENRES_DATA"))
        movies_data = load_json(application.config.get("MOVIES_DATA"))
        fill_db(Director, directors_data, db.session)
        fill_db(Genre, genres_data, db.session)
        fill_db(Movie, movies_data, db.session)
