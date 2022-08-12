from project.setup.db.db_init import db
from project.dao.main.director import DirectorDAO
from project.dao.main.genre import GenreDAO
from project.dao.main.movie import MovieDAO
from project.service.director import DirectorService
from project.service.genre import GenreService
from project.service.movie import MovieService


director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)
