from fastapi import FastAPI
from models import Product
from services.product_service import ProductService
import uvicorn

app = FastAPI()

# products = [
#     Product(id=1, name="Phone", description="This is a Phone", price=99, quantity=10),
#     Product(
#         id=2, name="Laptop", description="This is a Laptop", price=1000, quantity=11
#     ),
#     Product(id=3, name="Tablet", description="This is a Tablet", price=600, quantity=8),
# ]

product_service = ProductService()


# home page
@app.get("/")
def welcome_home():
    return "Welcome to the home page"


# get all product
@app.get("/products")
def get_all_products():
    return product_service.get_all_products()


# get product by id
@app.get("/product/{id}")
def get_product_by_id(id: int):
    return product_service.get_product_by_id(id)


# add a new product
@app.post("/add-product")
def add_product(product: Product):
    return product_service.add_product(product)


@app.put("/product")
def update_product(id: int, product: Product):
    return product_service.update_product(id, product)


@app.delete("/product/{id}")
def delete_product_by_id(id: int):
    return product_service.delete_product(id)


def main():
    # print("Hello from pythonproject!")
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
