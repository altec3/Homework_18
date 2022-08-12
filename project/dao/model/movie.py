from marshmallow import Schema, fields, validate

from project.setup.db_init import db
from project.dao.model.director import Director # noqa
from project.dao.model.genre import Genre # noqa


class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))

    genre = db.relationship("Genre")
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(max=255))
    description = fields.String(validate=validate.Length(max=255))
    trailer = fields.String(validate=validate.Length(max=255))
    year = fields.Integer()
    rating = fields.Integer()
    genre_id = fields.Integer()
    director_id = fields.Integer()
