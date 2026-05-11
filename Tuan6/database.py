from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
DATABASE_URL= "postgresql://postgres:123@localhost:5432/cleanfood"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db=SessionLocal() #mở session
    try:
        yield db
    finally:
        db.close()