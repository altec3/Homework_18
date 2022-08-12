from project.dao.main.director import DirectorDAO


class DirectorService:

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def create(self, data: dict):
        return self.dao.create(data)

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, did: int):
        return self.dao.get_by_id(did)

    def update(self, data: dict) -> bool:
        return self.dao.update(data)

    def delete(self, did: int) -> bool:
        return self.dao.delete(did)
