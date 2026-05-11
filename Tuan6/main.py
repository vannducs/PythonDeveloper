from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import get_db, engine, Base
from schemas import ( ProductCreate, ProductResponse, CategoryCreate, CategoryResponse)
from models import Product, Category

app= FastAPI(title="Clean Food API")

@app.post("/categories",response_model=CategoryResponse)
def create_category(data: CategoryCreate, db: Session = Depends(get_db)):
    new = Category(**data.model_dump()) #Dict
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@app.get("/categories", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()



@app.get("/products", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all() 

@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Không tìm thấy sản phẩm")
    return product

@app.post("/products", response_model=ProductResponse)
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    new = Product(**data.model_dump())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, data: ProductCreate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Không tìm thấy sản phẩm")
    for key, value in data.model_dump().items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Không tìm thấy sản phẩm")
    db.delete(product)
    db.commit()
    return {"message": f"Đã xóa sản phẩm id={product_id}"}