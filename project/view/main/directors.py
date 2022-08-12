from flask_restx import Namespace, Resource

from project.container import director_service
from project.dao.model.director import DirectorSchema

directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route("/")
class DirectorsView(Resource):

    @directors_ns.response(200, description="Возвращает список режиссеров")
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


@directors_ns.route("/<int:did>")
class DirectorView(Resource):

    @directors_ns.response(200, description="Возвращает режиссера по его ID")
    @directors_ns.response(404, description="Режиссер с данным ID не найден в базе")
    def get(self, did: int):
        director = director_service.get_by_id(did)
        return director_schema.dump(director), 200
