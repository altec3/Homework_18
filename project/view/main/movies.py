from flask import request
from flask_restx import Resource, Namespace

from project.container import movie_service
from project.dao.model.movie import MovieSchema

movies_ns: Namespace = Namespace("movies")

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movies_ns.route("/")
class MoviesView(Resource):

    @movies_ns.response(200, description="Возвращает список фильмов")
    def get(self):
        all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200

    @movies_ns.response(201, description="Фильм успешно добавлен в фильмотеку")
    @movies_ns.response(404, description="Ошибка добавления фильма в фильмотеку")
    def post(self):
        try:
            movie: dict = movie_schema.load(request.json)
            response = movie_service.create(movie)
        except Exception:
            return "", 400
        else:
            return movie_schema.dump(response), 201


@movies_ns.route("/<int:mid>")
class MovieView(Resource):

    @movies_ns.response(200, description="Возвращает фильм по его ID")
    @movies_ns.response(404, description="Фильм с данным ID не найден в фильмотеке")
    def get(self, mid: int):
        movie = movie_service.get_by_id(mid)
        return movie_schema.dump(movie), 200

    @movies_ns.response(204, description="Данные по фильму успешно обновлены")
    @movies_ns.response(404, description="Ошибка обновления данных фильма")
    def put(self, mid: int):
        data: dict = request.json
        data['id'] = mid
        if movie_service.update(data):
            return "", 204
        return "", 404

    @movies_ns.response(204, description="Фильм успешно удален из фильмотеки")
    @movies_ns.response(404, description="Фильм с данным ID не найден в фильмотеке")
    def delete(self, mid: int):
        if movie_service.delete(mid):
            return "", 204
        return "", 404

