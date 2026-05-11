from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, func, DateTime
from database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    slug = Column(String(100),unique=True)

    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(200),nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, default=0)
    create_at = Column(DateTime, default=func.now())
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="products")

    