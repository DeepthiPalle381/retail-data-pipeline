import pandas as pd
from pathlib import Path

CLEAN_DIR = Path("data/clean")
WAREHOUSE_DIR = Path("data/warehouse")

def load_clean_csv(name: str) -> pd.DataFrame:
    return pd.read_csv(CLEAN_DIR / f"clean_{name}")

def create_dim_users(users):
    dim = users[[
        "user_id", "name", "gender", "city", "signup_date"
    ]].drop_duplicates().reset_index(drop=True)

    return dim.rename(columns={
        "name": "user_name"
    })

def create_dim_products(products):
    dim = products[[
        "product_id", "product_name", "category", "price", "rating"
    ]].drop_duplicates().reset_index(drop=True)
    return dim

def create_fact_sales(orders, order_items):
    # Join order_items with orders on order_id
    fact = order_items.merge(
        orders,
        on="order_id",
        how="left"
    )

    # Normalize order_status values: strip spaces + Title case
    if "order_status" in fact.columns:
        fact["order_status"] = (
            fact["order_status"]
            .astype(str)
            .str.strip()
            .str.title()   # e.g. 'completed' -> 'Completed'
        )

    # Create line_amount column
    if "quantity" in fact.columns and "item_price" in fact.columns:
        fact["line_amount"] = fact["quantity"] * fact["item_price"]

    # Optional: try to order columns if they exist, but don't fail if some are missing
    preferred_order = [
        "order_item_id",
        "order_id",
        "user_id",
        "product_id",
        "order_date",
        "order_status",
        "quantity",
        "item_price",
        "line_amount",
        "total_amount",
    ]

    existing_cols = [c for c in preferred_order if c in fact.columns]
    remaining_cols = [c for c in fact.columns if c not in existing_cols]

    fact = fact[existing_cols + remaining_cols]

    return fact

def main():
    print("Loading cleaned data...")

    users = load_clean_csv("users.csv")
    products = load_clean_csv("products.csv")
    orders = load_clean_csv("orders.csv")
    order_items = load_clean_csv("order_items.csv")

    print("Creating dimension tables...")
    dim_users = create_dim_users(users)
    dim_products = create_dim_products(products)

    print("Creating fact table...")
    fact_sales = create_fact_sales(orders, order_items)

    print("Saving warehouse tables...")
    WAREHOUSE_DIR.mkdir(parents=True, exist_ok=True)

    dim_users.to_csv(WAREHOUSE_DIR / "dim_users.csv", index=False)
    dim_products.to_csv(WAREHOUSE_DIR / "dim_products.csv", index=False)
    fact_sales.to_csv(WAREHOUSE_DIR / "fact_sales.csv", index=False)

    print("✔ Transformation complete!")

if __name__ == "__main__":
    main()
