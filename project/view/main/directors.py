from flask_restx import Namespace, Resource

from project.container import director_service
from project.dao.model.director import DirectorSchema
from project.setup.api.models import error_api_model, director_api_model

directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route("/")
class DirectorsView(Resource):
    """Shows a list of all directors"""

    @directors_ns.marshal_list_with(director_api_model, code=200, description="OK")
    def get(self):
        """List all directors"""

        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


@directors_ns.route("/<int:did>")
class DirectorView(Resource):
    """Show a single director item"""

    @directors_ns.marshal_with(director_api_model, code=200, description="OK")
    @directors_ns.response(404, description="Not Found", model=error_api_model)
    def get(self, did: int):
        """Fetch a given resource"""

        director = director_service.get_by_id(did)
        return director_schema.dump(director), 200
