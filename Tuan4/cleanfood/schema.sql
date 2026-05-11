
CREATE TABLE IF NOT EXISTS categories (
    id   SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    slug VARCHAR(100) UNIQUE
);

CREATE TABLE IF NOT EXISTS products (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(200)   NOT NULL,
    price       DECIMAL(12, 0) NOT NULL CHECK (price >= 0),
    stock       INT            DEFAULT 0,
    category_id INT REFERENCES categories(id),
    created_at  TIMESTAMP DEFAULT NOW()
);