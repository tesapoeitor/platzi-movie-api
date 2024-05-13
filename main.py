from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from utils.jwt_manager import create_token, SECRET
from config.database import Base, engine
from middlewares import ErrorHandler
from routers import movie_router, auth_router

app = FastAPI()
app.title = 'Mi aplicación con FastApi'
app.version = '0.0.1'

app.add_middleware(ErrorHandler)

app.include_router(movie_router)
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    }
]

@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1 style="color: orange;">Hello World</h1>')
