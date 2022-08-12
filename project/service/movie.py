from project.dao.main.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def create(self, data: dict):
        return self.dao.create(data)

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, mid: int):
        return self.dao.get_by_id(mid)

    def update(self, data: dict) -> bool:
        return self.dao.update(data)

    def delete(self, mid: int) -> bool:
        return self.dao.delete(mid)
