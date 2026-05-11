from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.order import Order, OrderItem
from app.models.product import Product
from app.schemas.order import OrderItemCreate, OrderResponse

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/checkout", response_model=OrderResponse)
def checkout(items: List[OrderItemCreate], db: Session = Depends(get_db)):
    try:
        for item in items:
            product = db.query(Product).filter(Product.id == item.product_id).first()

            if not product:
                raise HTTPException(
                    status_code=404,
                    detail=f"Không tìm thấy sản phẩm id={item.product_id}"
                )
            if product.stock < item.quantity:
                raise HTTPException(
                    status_code=400,
                    detail=f"{product.name}: không đủ hàng (còn {product.stock})"
                )
        new_order = Order()
        db.add(new_order)
        db.flush() 

        for item in items:
            product = db.query(Product).filter(Product.id == item.product_id).first()
            product.stock -= item.quantity  

            order_item = OrderItem(
                order_id=new_order.id,
                product_id=item.product_id,
                quantity=item.quantity
            )
            db.add(order_item)

        db.commit()
        db.refresh(new_order)
        return new_order

    except HTTPException:
        db.rollback()
        raise