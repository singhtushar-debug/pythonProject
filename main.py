from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
from contextlib import asynccontextmanager
from models import Product
from sqlalchemy.ext.asyncio import AsyncSession
from services.product_service import ProductService
from dotenv import load_dotenv
from db import get_db, engine
import os
import database_models
import uvicorn
import jwt

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("ALGORITHM")

security = HTTPBearer()


# create tables
@asynccontextmanager
async def lifeSpan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(database_models.Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifeSpan)

product_service = ProductService()


@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    """
    Middleware to handle JWT authentication.

    This middleware intercepts incoming HTTP requests to validate a Bearer token provided in the 'Authorization' header.

    Args:
        request: The incoming request object.
        call_next: The function that passes the request to the next middleware or path operation.
    Returns:
        Response: The final processed response if authentication is successful.
        JSONResponse: A 401 Unauthorized access response if authentication fails.

    How it works:
        1.Check if the path is in the public_paths list.
        2.Validates the presence and format of the 'Bearer' token.
        3.Decodes the JWT using the secret key and algorithm.
        4.Return the response.
    """
    public_paths = ["/", "/docs", "/login", "/openapi.json"]
    if request.url.path in public_paths:
        return await call_next(request)
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer"):
        return JSONResponse(
            status_code=401,
            content={
                "detail": "Missing or invalid authentication token. Please login !"
            },
        )
    token = auth_header.split(" ")[1]
    try:
        data = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        request.state.user = data
    except jwt.ExpiredSignatureError:
        return JSONResponse(
            status_code=401, content={"detail": "Token is expired,login again"}
        )
    except jwt.InvalidTokenError:
        return JSONResponse(status_code=401, content={"detail": "Invalid token"})
    response = await call_next(request)
    return response


# home page
@app.get("/")
async def welcome_home():
    return "Welcome to the home page"


@app.post("/login")
async def login():
    """
    Function to simulate a user login.
    Returns:
        token: A jwt token.
    """
    data = {"username": "tushar singh"}
    token = jwt.encode(data, JWT_SECRET, algorithm="HS256")
    return {"token": token}


# get all product
@app.get("/products", dependencies=[Depends(security)])
async def get_all_products(db: AsyncSession = Depends(get_db)):
    return await product_service.get_all_products(db)


# get product by id
@app.get("/product/{id}", dependencies=[Depends(security)])
async def get_product_by_id(id: int, db: AsyncSession = Depends(get_db)):
    return await product_service.get_product_by_id(id, db)


# add a new product
@app.post("/add-product", dependencies=[Depends(security)])
async def add_product(product: Product, db: AsyncSession = Depends(get_db)):
    return await product_service.add_product(product, db)


@app.put("/product", dependencies=[Depends(security)])
async def update_product(id: int, product: Product, db: AsyncSession = Depends(get_db)):
    return await product_service.update_product(id, product, db)


@app.delete("/product/{id}", dependencies=[Depends(security)])
async def delete_product_by_id(id: int, db: AsyncSession = Depends(get_db)):
    return await product_service.delete_product(id, db)


def main():
    # print("Hello from pythonproject!")
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
