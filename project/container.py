from project.setup.db_init import db
from project.dao.movie import MovieDAO
from project.dao.director import DirectorDAO
from project.service.movie import MovieService
from project.service.director import DirectorService


director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)
