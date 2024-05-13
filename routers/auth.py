from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token, SECRET
from schemas import User

auth_router = APIRouter()

@auth_router.post('/login', tags=['Auth'], status_code=200)
def login(user: User):
    if user.email == 'admin@gmail.com' and user.password == 'admin':
        token: str = create_token(user.model_dump(), SECRET)
        return JSONResponse(status_code=200, content=token)