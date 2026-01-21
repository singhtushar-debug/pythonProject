from models import Product
from typing import List


class ProductService:
    """
    Provides business logic for managing products.
    """

    def __init__(self):
        self.products: List[Product] = [
            Product(
                id=1, name="Phone", description="This is a Phone", price=99, quantity=10
            ),
            Product(
                id=2,
                name="Laptop",
                description="This is a Laptop",
                price=1000,
                quantity=11,
            ),
            Product(
                id=3,
                name="Tablet",
                description="This is a Tablet",
                price=600,
                quantity=8,
            ),
        ]

    def get_all_products(self):
        """
        Fetches the complete list of products.
        Returns:
                List[Products]: A list containing all product records.
        """
        return self.products

    def get_product_by_id(self, id: int):
        """
        Fetches a product using its unique id.
        Args:
            id: The unique integer id of the product.
        Returns:
            Product: The matching product object if found,otherwrise returns "product not found".
        """
        for product in self.products:
            if product.id == id:
                return product
        return "Product not found"

    def add_product(self, product: Product):
        """
        Add a new product to the product list.
        Args:
            Product: The product to be added.
        Returns:
            Product: The product to be added.
        """
        self.products.append(product)
        return product

    def update_product(self, id: int, product: Product):
        """
        Updates an existing product record.
        Args:
            id: The id of the product to be updated.
            Product: The updated product.
        Returns:
            Product: The updated prodcut if successfull,otherwise returns "Product not found".

        """
        for i in range(len(self.products)):
            if self.products[i].id == id:
                self.products[i] = product
                return product
        return "Product not found"

    def delete_product(self, id: int):
        """
        Removes a product record from the inventory.
        Args:
            id: The id of the product to be deleted.
        Returns:
            Product: The removed product if successfull, otherwise string "Product not found"
        """
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                return product
        return "Product not found"
