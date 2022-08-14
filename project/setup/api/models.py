from flask_restx import Model, fields

from project.setup.api import api

error_api_model: Model = api.model('Сообщение об ошибке', {
    'message': fields.String(required=True, example='Error description'),
    'errors': fields.Wildcard(fields.String, required=False),
})

director_api_model: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Тейлор Шеридан'),
})

genre_api_model: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

movie_api_model: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=255, example='Йеллоустоун'),
    'description': fields.String(
        required=True,
        example='Владелец ранчо пытается сохранить землю своих предков. '
                'Кевин Костнер в неовестерне от автора «Ветреной реки»'
    ),
    'trailer': fields.String(max_length=255, example='https://www.youtube.com/watch?v=UKei_d0cbP4'),
    'year': fields.Integer(required=True, min=0, example=2018),
    'rating': fields.Integer(required=True, min=0.0, max=10.0, example=8.6),
    'genre': fields.Nested(genre_api_model, required=True),
    'director': fields.Nested(director_api_model, required=True),
})
