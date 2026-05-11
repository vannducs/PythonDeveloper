from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routers.categories import router as categories
from app.routers.products import router as products
from app.routers.orders import router as orders
from app.exceptions import ProductNotFoundError
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Shop CleanFood", version="1.0.0")

@app.exception_handler(ProductNotFoundError)
async def product_not_found_handler(request: Request, exc: ProductNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Product Not Found",
            "message": f"Không tìm thấy sản phẩm với ID = {exc.product_id}",
            "status_code": 404
        }
    )

@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "Shop CleanFood đang chạy!"}

app.include_router(categories)
app.include_router(products)
app.include_router(orders)