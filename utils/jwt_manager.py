from jwt import encode, decode

SECRET = 'MY_SECRET_KEY'

def create_token(data: dict, secret: str) -> str:
    token: str = encode(payload=data, key=secret, algorithm="HS256")
    return token

def validate_token(token: dict, secret: str) -> dict:
    data: dict = decode(token, key=secret, algorithms=['HS256'])
    return data