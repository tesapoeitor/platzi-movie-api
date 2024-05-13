from config.database import Session
from models.movie import Movie as MovieModel
from schemas import Movie

class MovieService():
    def __init__(self) -> None:
        self.db = Session()
    
    def get_movies(self):
        return self.db.query(MovieModel).all()
    
    def get_movie(self, id: int):
        return self.db.query(MovieModel).filter(MovieModel.id == id).first()
    
    def get_movie_by_category(self, category: str):
        return self.db.query(MovieModel).filter(MovieModel.category == category).all()
    
    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()
        return
    
    def update_movie(self, id: int, data: Movie):
        movie = self.get_movie(id)
        movie.title = data.title
        movie.overview = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()
        return
    
    def delete_movie(self, id: int):
        movie = self.get_movie(id)
        self.db.delete(movie)
        self.db.commit()
        return