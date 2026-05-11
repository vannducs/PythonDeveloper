from fastapi import FastAPI, HTTPException
from schemas import ProductCreate, ProductResponse

app = FastAPI(title="Clean Food API")

products = []
next_id=1

@app.get("/")
def root():
    return {"message":"Clean Food API đang chạy"}

@app.get("/product/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    for p in products:
        if p["id"] == product_id:
            return p
    raise HTTPException(status_code=404, detail="Không tìm thấy sản phẩm")

@app.post("/products",response_model=ProductResponse)
def create_product(data: ProductCreate):
    global next_id
    new = {"id": next_id, **data.model_dump()} #lấy dữ liệu từ request
    products.append(new) 
    next_id +=1
    return new

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i, p in enumerate(products):
        if p["id"] == product_id:
            products.pop(i)
            return {"message":f"Đã xóa id={product_id}"}   
    raise HTTPException(status_code=404, detail="Không tìm thấy sản phẩm")