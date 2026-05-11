from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(min_length=1,max_length=50, description="Tên sản phẩm")
    price: int = Field(gt=0, description="Giá >0")
    stock: int = Field(ge=0, description="Tồn kho >=0")
    category: str = Field(min_length=1, description="Danh mục")

class ProductResponse(BaseModel):
    id: int
    name: str
    price: int
    stock: int
    category: str