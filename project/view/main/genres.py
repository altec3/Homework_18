from flask_restx import Resource, Namespace

from project.container import genre_service
from project.dao.model.genre import GenreSchema

genres_ns: Namespace = Namespace("genres")

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


@genres_ns.route("/")
class GenresView(Resource):

    @genres_ns.response(200, description="Возвращает список жанров")
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genres_ns.route("/<int:gid>")
class GenreView(Resource):

    @genres_ns.response(200, description="Возвращает жанр по его ID")
    @genres_ns.response(404, description="Жанр с данным ID не найден в базе")
    def get(self, gid: int):
        genre = genre_service.get_by_id(gid)
        return genre_schema.dump(genre), 200
