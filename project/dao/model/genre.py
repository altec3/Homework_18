# Models for SQLAlchemy and Marshmallow

from marshmallow import Schema, fields, validate

from project.setup.db import db


class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'<Genre {self.name}>'


class GenreSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(validate=validate.Length(max=255))
