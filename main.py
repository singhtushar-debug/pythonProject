from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from models import Product
from sqlalchemy.ext.asyncio import AsyncSession
from services.product_service import ProductService
from db import get_db, engine
import database_models
import uvicorn


# create tables
@asynccontextmanager
async def lifeSpan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(database_models.Base.metadata.create_all)
    yield


app = FastAPI()

product_service = ProductService()


# home page
@app.get("/")
async def welcome_home():
    return "Welcome to the home page"


# get all product
@app.get("/products")
async def get_all_products(db: AsyncSession = Depends(get_db)):
    return await product_service.get_all_products(db)


# get product by id
@app.get("/product/{id}")
async def get_product_by_id(id: int, db: AsyncSession = Depends(get_db)):
    return await product_service.get_product_by_id(id, db)


# add a new product
@app.post("/add-product")
async def add_product(product: Product, db: AsyncSession = Depends(get_db)):
    return await product_service.add_product(product, db)


@app.put("/product")
async def update_product(id: int, product: Product, db: AsyncSession = Depends(get_db)):
    return await product_service.update_product(id, product, db)


@app.delete("/product/{id}")
async def delete_product_by_id(id: int, db: AsyncSession = Depends(get_db)):
    return await product_service.delete_product(id, db)


def main():
    # print("Hello from pythonproject!")
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
