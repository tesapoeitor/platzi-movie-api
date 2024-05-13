from sqlalchemy import Column, Integer, String, Float
from config.database import Base

class Movie(Base):
    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)
    
    def __repr__(self):
        return f'<Movie(id={self.id}, title={self.title}, overview={self.overview}, year={self.year}, rating={self.rating}, category={self.category})>'