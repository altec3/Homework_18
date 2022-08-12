from project.dao.model.movie import Movie

from flask_sqlalchemy import SQLAlchemy


class MovieDAO:

    def __init__(self, session: SQLAlchemy().session):
        self.session = session

    def create(self, data: dict) -> Movie:
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

        return movie

    def get_all(self) -> list[Movie]:
        return self.session.query(Movie).all()

    def get_by_id(self, did: int) -> Movie:
        return self.session.query(Movie).get_or_404(did)

    def update(self, data: dict) -> bool:
        mid = data.get('id')
        if self.session.query(Movie).filter(Movie.id == mid).update(data):
            self.session.commit()
            return True

        return False

    def delete(self, mid: int) -> bool:
        if self.session.query(Movie).filter(Movie.id == mid).delete():
            self.session.commit()
            return True

        return False
