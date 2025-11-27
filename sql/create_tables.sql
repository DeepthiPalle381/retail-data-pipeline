-- Warehouse schema documentation

-- Users Dimension
CREATE TABLE dim_users (
    user_id TEXT,
    user_name TEXT,
    gender TEXT,
    city TEXT,
    signup_date TEXT
);

-- Products Dimension
CREATE TABLE dim_products (
    product_id TEXT,
    product_name TEXT,
    category TEXT,
    price DOUBLE PRECISION,
    rating DOUBLE PRECISION
);

-- Sales Fact Table
CREATE TABLE fact_sales (
    order_item_id TEXT,
    order_id TEXT,
    user_id TEXT,
    product_id TEXT,
    order_date TEXT,
    order_status TEXT,
    quantity INTEGER,
    item_price DOUBLE PRECISION,
    line_amount DOUBLE PRECISION,
    total_amount DOUBLE PRECISION
);
