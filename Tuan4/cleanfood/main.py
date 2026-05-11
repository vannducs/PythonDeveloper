import psycopg2 as psy

DB_CONFIG = {
    "host": "localhost",
    "dbname":"cleanfood",
    "user":"postgres",
    "password":123,
    "port":5432,
}

def add_category(name, slug):
    with psy.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "insert into categories (name,slug) " \
                "values (%s, %s) returning id",(name,slug),
            )
            new_id = cur.fetchone()[0]
        conn.commit()
    print(f"Thêm category: {name} (id={new_id})")
    return new_id

def add_product(name, price, stock, category_id):
    with psy.connect(**DB_CONFIG) as conn: #mở kết nối
        with conn.cursor() as cur: #mở cursor
            cur.execute(     #gửi lệnh
                """
                insert into products(name,price, stock, category_id)
                values (%s, %s, %s, %s)
                returning id
                """,
                (name, price, stock, category_id),
            )
            new_id = cur.fetchone()[0] #thực thi lệnh
        conn.commit() #lưu kết quả - đóng kết nối
    print(f"Theem sản phẩm: {name} (id={new_id})")

def show_products():
    with psy.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select p.id, p.name, p.price, p.stock, c.name
                from products p
                left join categories c 
                on p.categories_id = c.id
                order by p.id
                """
                        )
            rows = cur.fetchall()
    print ("-----Kho hàng---")
    for id, name, price, stock, category in rows:
        print(f"[{id}] {name:<15} {int(price):>10,}vnd | Còn lại: {stock} | {category}")

if __name__ == "__main__":
    rau_id = add_category("Rau củ quả", "rau-cu-qua")
    thit_id = add_category("Thịt cá", "thit-ca")

    add_product("Rau cải", 20000, 100, rau_id)
    add_product("Rau muống", 10000, 200, rau_id)
    add_product("Thịt lợn", 150000, 50, thit_id)
    show_products()
