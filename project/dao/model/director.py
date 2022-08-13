# Models for SQLAlchemy and Marshmallow

from marshmallow import Schema, fields, validate

from project.setup.db import db


class Director(db.Model):
    __tablename__ = 'director'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'<Director {self.name}>'


class DirectorSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(validate=validate.Length(max=255))
