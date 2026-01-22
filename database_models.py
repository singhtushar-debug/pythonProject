# from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class ProductDB(Base):
    __tablename__ = "product"

    # id = Column(Integer, primary_key=True)
    # name = Column(String)
    # description = Column(String)
    # price = Column(Float)
    # quantity = Column(Integer)
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[float]
    quantity: Mapped[int]
