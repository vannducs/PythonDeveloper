from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.category import CategoryCreate, CategoryResponse
from app.models.category import Category

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("/", response_model=CategoryResponse)
def create_category(data: CategoryCreate, db: Session = Depends(get_db)):
    new = Category(**data.model_dump())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@router.get("/", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()