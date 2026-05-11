from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, func
from app.database import Base
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=True)
    stock = Column(Integer, default=0)
    create_at = Column(DateTime, default=func.now()) 
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="products")