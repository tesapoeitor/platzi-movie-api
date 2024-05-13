from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from utils.jwt_manager import validate_token, SECRET

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials, SECRET)
        if data['email'] != 'admin@gmail.com':
            raise HTTPException(status_code=403, detail='Credenciales son invalidas')