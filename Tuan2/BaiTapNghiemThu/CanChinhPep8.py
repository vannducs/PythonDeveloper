products = [
    {"id": 1, "name": "Rau cải", "price": 20000},
    {"id": 2, "name": "Thịt heo", "price": 150000},
    {"id": 3, "name": "Cá thu", "price": 80000},
]


# Hiện tên sản phẩm
def show(products):
    pro = [p["name"] for p in products]
    print(pro)


def edit(products, product_id, new_price):
    for p in products:
        if p["id"] == product_id:
            p["price"] = new_price
            print(f"Đã cập nhật: {new_price}đ")


def delete(products, product_id):
    for i, p in enumerate(products):
        if p["id"] == product_id:
            print(f"Đã xóa: {products.pop(i)['name']}")
