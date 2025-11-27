import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
CLEAN_DIR = Path("data/clean")

FILES = [
    "users.csv",
    "products.csv",
    "orders.csv",
    "order_items.csv",
    "reviews.csv",
    "events.csv",
]

def ingest_file(filename: str) -> None:
    input_path = RAW_DIR / filename
    output_path = CLEAN_DIR / f"clean_{filename}"

    # Load the raw CSV
    df = pd.read_csv(input_path)

    # Basic cleaning:
    # - Remove completely empty rows
    # - Reset index
    df = df.dropna(how="all").reset_index(drop=True)

    # Make output directory if not exists
    CLEAN_DIR.mkdir(parents=True, exist_ok=True)

    # Save cleaned output
    df.to_csv(output_path, index=False)
    print(f"📁 Saved cleaned file: {output_path} ({len(df)} rows)")

def main():
    print("Starting ingestion...")
    for file in FILES:
        ingest_file(file)
    print("Ingestion complete!")

if __name__ == "__main__":
    main()
