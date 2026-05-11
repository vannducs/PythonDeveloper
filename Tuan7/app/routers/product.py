from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db                        
from app.schemas.product import ProductCreate, ProductResponse
from app.models.product import Product  
from app.exceptions import ProductNotFoundError              

router = APIRouter(prefix="/products", tags=["products"])  

@router.get("/", response_model=list[ProductResponse])   
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise ProductNotFoundError(product_id=product_id)
    return product

@router.post("/", response_model=ProductResponse)
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    new = Product(**data.model_dump())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, data: ProductCreate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise ProductNotFoundError(product_id=product_id)
    for key, value in data.model_dump().items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Không tìm thấy sản phẩm")
    db.delete(product)
    db.commit()
    return {"message": f"Đã xóa sản phẩm id={product_id}"}