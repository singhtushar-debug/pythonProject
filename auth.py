from fastapi import Depends, HTTPException
from typing import Annotated
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import jwt
import os

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_token(data: dict):
    """
    Creates a signed JWT for user authentication.
    Args:
        data(dict): The payload to encode.
    Returns:
        str: An encoded JWT string (access_token).
    """
    return jwt.encode(data, JWT_SECRET, algorithm=ALGORITHM)


def get_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    Authenticates the user by decoding and validating the provided JWT.
    This function acts as a FastAPI dependency.

    Args:
        token(str): The Bearer token extracted from the Authentication header.
    Returns:
        dict: A dictionary containing user information ( {"username": "Tushar"} ).
    Raises:
        HTTPException: 401 Unauthorized if the token is invalid or expired.
    """
    try:
        data = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        username = data.get("username")
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired !")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": username}
