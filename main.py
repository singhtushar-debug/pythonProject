from fastapi import FastAPI, Depends
from models import Product
from sqlalchemy.orm import Session
from services.product_service import ProductService
from db import get_db, engine
import database_models
import uvicorn

# create tables
database_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

product_service = ProductService()


# home page
@app.get("/")
def welcome_home():
    return "Welcome to the home page"


# get all product
@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    return product_service.get_all_products(db)


# get product by id
@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    return product_service.get_product_by_id(id, db)


# add a new product
@app.post("/add-product")
def add_product(product: Product, db: Session = Depends(get_db)):
    return product_service.add_product(product, db)


@app.put("/product")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    return product_service.update_product(id, product, db)


@app.delete("/product/{id}")
def delete_product_by_id(id: int, db: Session = Depends(get_db)):
    return product_service.delete_product(id, db)


def main():
    # print("Hello from pythonproject!")
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
