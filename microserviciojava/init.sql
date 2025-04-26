CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    category_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS suppliers (
    id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    category_id INT REFERENCES categories(id),
    supplier_id INT REFERENCES suppliers(id)
);

CREATE TABLE IF NOT EXISTS inventory (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id),
    quantity INT
);


INSERT INTO categories (category_name)
SELECT 'Category ' || g FROM generate_series(1, 100) g;

INSERT INTO suppliers (supplier_name)
SELECT 'Supplier ' || g FROM generate_series(1, 100) g;


INSERT INTO products (name, category_id, supplier_id)
SELECT 'Product ' || g, (g % 100) + 1, (g % 100) + 1 FROM generate_series(1, 20000) g;
