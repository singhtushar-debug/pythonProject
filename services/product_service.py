from models import Product
from sqlalchemy.orm import Session
from sqlalchemy import select, update

# from sqlalchemy import select
from database_models import ProductDB


class ProductService:
    """
    Provides business logic for managing products.
    """

    def get_all_products(self, db: Session):
        """
        Fetches the complete list of products.
        Returns:
                List[Products]: A list containing all product records.
        """
        result = db.execute(select(ProductDB))
        return result.scalars().all()

    def get_product_by_id(self, id: int, db: Session):
        """
        Fetches a product using its unique id.
        Args:
            id: The unique integer id of the product.
        Returns:
            Product: The matching product object if found,otherwrise returns NULL.
        """
        return db.get(ProductDB, id)

    def add_product(self, product: Product, db: Session):
        """
        Add a new product to the product list.
        Args:
            Product: The product to be added.
        Returns:
            Product: The product to be added.
        """
        db_product = ProductDB(
            **product.model_dump()
        )  # convert pydantic model product into database model productdb
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    def update_product(self, id: int, product: Product, db: Session):
        """
        Updates an existing product record.
        Args:
            id: The id of the product to be updated.
            Product: The updated product.
        Returns:
            Product: The updated prodcut if successfull,otherwise returns NULL.

        """

        upd_stmt = (
            update(ProductDB)
            .where(ProductDB.id == id)
            .values(**product.model_dump())
            .returning(ProductDB)
        )
        result = db.execute(upd_stmt)
        db.commit()
        return result.scalar_one_or_none()

    def delete_product(self, id: int, db: Session):
        """
        Removes a product record from the inventory.
        Args:
            id: The id of the product to be deleted.
        Returns:
            Product: The removed product if successfull, otherwise None.
        """
        db_product = self.get_product_by_id(id, db)
        if db_product:
            db.delete(db_product)
            db.commit()
            return db_product
        return None
