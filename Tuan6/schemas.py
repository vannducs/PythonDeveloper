from pydantic import BaseModel, Field
from typing import Optional

class CategoryCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    slug: str = Field(min_length=1, max_length=100)

class CategoryResponse(BaseModel):
    id: int
    name: str
    slug: str
    model_config = {"from_attributes":True}

class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    price: int= Field(gt=0)
    stock: int=Field(ge=0)
    category_id: int

class ProductResponse(BaseModel):
    id: int
    name: str
    price: int
    stock: int
    category_id: int
    model_config ={"from_attributes":True}