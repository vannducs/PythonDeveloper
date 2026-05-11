from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
     name: str = Field(min_length=1, max_length=50)
     price: int = Field(gt=0)
     stock: int = Field(ge=0)
     category_id: int

class ProductResponse(BaseModel):
     id: int
     name: str
     price: int
     stock: int
     category_id: int
     model_config ={"from_attributes": True}     
