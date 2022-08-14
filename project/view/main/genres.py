from flask_restx import Resource, Namespace

from project.container import genre_service
from project.dao.model.genre import GenreSchema
from project.setup.api.models import error_api_model, genre_api_model

genres_ns: Namespace = Namespace("genres")

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


@genres_ns.route("/")
class GenresView(Resource):
    """Shows a list of all genres"""

    @genres_ns.marshal_list_with(genre_api_model, code=200, description='OK')  # -> to Frontend
    def get(self):
        """List all genres"""

        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genres_ns.route("/<int:gid>")
class GenreView(Resource):
    """Show a single genre item"""

    @genres_ns.marshal_with(genre_api_model, code=200, description='OK')  # -> to Frontend
    @genres_ns.response(404, description="Not Found", model=error_api_model)
    def get(self, gid: int):
        """Fetch a given resource"""

        genre = genre_service.get_by_id(gid)
        return genre_schema.dump(genre), 200
