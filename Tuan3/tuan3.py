class Product:
    def __init__(self,id, name, price, stock):
        self.id=id
        self.name=name
        self.price=price
        self.stock=stock
        
    def show(self):
        print(f"[{self.id}] {self.name:<15} {self.price:>10,}vnd {self.stock}")

    def is_cheap(self):
        return self.price<50000
    
    @property
    def stock_value(self):
        return self.price*self.stock

    

class InventoryManager:
    def __init__(self):
        self.products=[] #Rỗng

    def add(self, product):
        self.products.append(product)
        print(f"Đã thêm: {product.name}")

    def delete(self, product_id):
        for i, p in enumerate(self.products):
            if p.id==product_id:
                removed=self.products.pop(i)
                print(f"Đã xóa: {removed.name}")
                return
        print("Không tìm thấy")

    def search(self, keyword):
        return [p for p in self.products if keyword.lower() in p.name.lower()]

    def show_all(self):
        print("\n===== KHO HÀNG =====")
        for p in self.products:
            print(f"[{p.id}] {p.name:<15} {p.price:>10,}vnd")

    @property
    def total_stock_value(self):
        return sum(p.stock_value for p in self.products)


p = Product(1, "Rau cải",20000,100)
print(p.stock_value) 

manager = InventoryManager()
manager.add(p)
print(manager.total_stock_value)