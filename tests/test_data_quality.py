import pandas as pd

def test_users_have_valid_gender():
    df = pd.read_csv("data/warehouse/dim_users.csv")
    valid = {"Male", "Female", "Other"}
    assert set(df["gender"]).issubset(valid), "Invalid gender values found"

def test_products_have_positive_price():
    df = pd.read_csv("data/warehouse/dim_products.csv")
    assert (df["price"] >= 0).all(), "Negative price found"

def test_order_status_valid():
    df = pd.read_csv("data/warehouse/fact_sales.csv")
    valid = {"Completed", "Cancelled", "Returned", "Processing", "Shipped"}
    assert set(df["order_status"]).issubset(valid), "Unexpected order status value found"

