products = [
    {"id": 1, "name": "Rau cải",   "price": 20000},
    {"id": 2, "name": "Thịt heo",  "price": 150000},
    {"id": 3, "name": "Cá thu",    "price": 80000},
    {"id": 4, "name": "Rau muống", "price": 10000},
    {"id": 5, "name": "Cà chua",   "price": 15000},
]

#Tìm kiếm theo tên
result1 = [p for p in products if "Rau cải" in p["name"]]
print(result1)
#Theo giá chỉ lấy tên và giá
result2 = [{p["name"]: p["price"]} for p in products if p["price"]<20000]
print(result2) 
#Tăng giá sp thêm 500
result3 = [{**p,"price":p["price"]+500} for p in products if p["name"]=="Rau cải"]
print(result3)
