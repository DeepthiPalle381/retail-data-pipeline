-- 1. Total Revenue by Category
SELECT
    p.category,
    SUM(f.line_amount) AS revenue
FROM fact_sales f
JOIN dim_products p ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;

-- 2. Top 10 Products by Revenue
SELECT
    p.product_name,
    SUM(f.line_amount) AS revenue
FROM fact_sales f
JOIN dim_products p ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 10;

-- 3. Daily Revenue Trend
SELECT
    DATE(f.order_date) AS day,
    SUM(f.line_amount) AS daily_revenue
FROM fact_sales f
GROUP BY DATE(f.order_date)
ORDER BY day;

-- 4. Customer Lifetime Value
SELECT
    u.user_id,
    u.user_name,
    SUM(f.line_amount) AS lifetime_value
FROM fact_sales f
JOIN dim_users u ON f.user_id = u.user_id
GROUP BY u.user_id, u.user_name
ORDER BY lifetime_value DESC;

-- 5. Order Status Breakdown
SELECT
    order_status,
    COUNT(*) AS count_orders
FROM fact_sales
GROUP BY order_status;
