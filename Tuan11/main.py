from fastapi import FastAPI, HTTPException

app = FastAPI()
products = {}

@app.post("/products/{product_id}")
def create_product(product_id: int, name: str):
    products[product_id] = {
        "id": product_id,
        "name": name
    }

    return products[product_id]

@app.get("/products/{product_id}")
def get_product(product_id: int):

    product = products.get(product_id)
    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return product

@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    product = products.get(product_id)
    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    del products[product_id]
    return {
        "message": "Deleted successfully"
    }