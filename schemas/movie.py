from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2024)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=3, max_length=15)
    
    class Config:
        json_schema_extra = {
            'example': {
                'id': 1,
                'title': 'Mi película',
                'overview': 'Descripción de la película',
                'year': 2024,
                'rating': 3.5,
                'category': 'Acción'
            }
        }

