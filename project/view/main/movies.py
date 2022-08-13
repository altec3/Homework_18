from flask import request, current_app as app, url_for
from flask_restx import Resource, Namespace

from project.container import movie_service
from project.dao.model.movie import MovieSchema

movies_ns: Namespace = Namespace("movies")

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movies_ns.route("/")
class MoviesView(Resource):

    @movies_ns.response(200, description="OK")
    def get(self):

        page = request.args.get("page", 1, type=int)
        fields = {}

        if request.args.get("director_id"):
            fields["director_id"] = int(request.args.get("director_id"))
        if request.args.get("genre_id"):
            fields["genre_id"] = int(request.args.get("genre_id"))
        if request.args.get("year"):
            fields["year"] = int(request.args.get("year"))

        if fields:
            movies = movie_service.get_by_fields(page, app.config.get("MOVIES_PER_PAGE"), fields)
        else:
            movies = movie_service.get_all(page, app.config.get("MOVIES_PER_PAGE"))

        return movies_schema.dump(movies), 200

    @movies_ns.response(201, description="Created", headers={'Location': 'The URL of a newly created movie'})
    @movies_ns.response(404, description="Not Found")
    def post(self):
        try:
            movie: dict = movie_schema.load(request.json)
            response = movie_service.create(movie)
        except Exception:
            return "", 400
        else:
            return movie_schema.dump(response), 201, {'Location': url_for('movies_movie_view', mid=response.id)}


@movies_ns.route("/<int:mid>")
class MovieView(Resource):

    @movies_ns.response(200, description="OK")
    @movies_ns.response(404, description="Not Found")
    def get(self, mid: int):
        movie = movie_service.get_by_id(mid)
        return movie_schema.dump(movie), 200

    @movies_ns.response(204, description="No Content")
    @movies_ns.response(404, description="Not Found")
    def put(self, mid: int):
        data: dict = request.json
        data['id'] = mid
        if movie_service.update(data):
            return "", 204
        return "", 404

    @movies_ns.response(204, description="No Content")
    @movies_ns.response(404, description="Not Found")
    def delete(self, mid: int):
        if movie_service.delete(mid):
            return "", 204
        return "", 404

