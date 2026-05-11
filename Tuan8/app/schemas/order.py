from pydantic import BaseModel, Field
from typing import List

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)

class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    model_config = {"from_attributes": True}

class OrderResponse(BaseModel):
    id: int
    items: List[OrderItemResponse]
    model_config = {"from_attributes": True}