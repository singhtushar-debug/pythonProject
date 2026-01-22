from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_url = "postgresql://postgres:PGtushar123@localhost:5432/ProductInventory"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=True, bind=engine)


def get_db():
    db = session()
    yield db
    db.close()
