import psycopg2 as psy

DB_CONFIG = {
    "host": "localhost",
    "dbname": "cleanfood",
    "user": "postgres",
    "password": 123,
    "port": 5432,
}
def add_product():
    name=input("Tên món ăn: ")
    price=int(input("Đơn giá: "))
    stock= int(input("Số lượng: "))

    with psy.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "insert into products (name, price, stock) values (%s, %s, %s) returning id",
                (name, price, stock),
            )
            new_id=cur.fetchone()[0]
        conn.commit()

    print(f"Đã thêm {name} vào DB (id={new_id})")


if __name__ == "__main__":
    add_product()