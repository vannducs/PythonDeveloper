product = {
    "id": 1,
    "name": "Táo",
    "price": 10000,
}
print(product["name"],product["price"])
#Sửa giá trị
product["price"]=5000
#Thêm key mới
product["stock"]=70
del product["stock"] #xóa key
print(product)