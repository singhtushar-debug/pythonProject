from fastapi import FastAPI
from models import Product
import uvicorn

app = FastAPI() 

products = [
    Product(id = 1,name = "Phone",description = "This is a Phone",price = 99,quantity = 10),
    Product(id = 2,name = "Laptop",description = "This is a Laptop",price = 1000,quantity = 11),
    Product(id = 3,name = "Tablet",description = "This is a Tablet",price = 600,quantity = 8)
]

#home page
@app.get('/')
def welcome_home():
    return "Welcome to the home page"

#get all product
@app.get('/products')
def get_all_products():
    return products

#get product by id
@app.get('/product/{id}')
def get_product_by_id(id:int):
    for product in products:
        if product.id == id:
            return product
    return "No product found"

#add a new product
@app.post('/add-product')
def add_product(Product:Product):
    products.append(Product)
    return "Product added successfully"

@app.put('/product')
def update_product(id:int,Product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = Product
            return "Product updated successfully"
    return "Product not found"

@app.delete('/product/{id}')
def delete_product_by_id(id:int):
    for product in products:
        if product.id == id:
            products.remove(product)
            return "product deleted successfully"
    return "product not found"

def main():
    print("Hello from pythonproject!")
    uvicorn.run(app,host='127.0.0.1',port=8000)


if __name__ == "__main__":
    main()
