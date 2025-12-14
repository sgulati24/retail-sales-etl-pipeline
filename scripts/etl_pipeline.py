import pandas as pd

# 1. Load the dataset
def extract_data(path):
    print("Loading data...")
    df = pd.read_csv(path, encoding="ISO-8859-1")
    return df

# 2. Clean column names
def clean_column_names(df):
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df

# 3. Create dim_customers table
def create_dim_customers(df):
    print("Creating dim_customers table...")

    customers = df[[
        'customer_id',
        'customer_name',
        'segment',
        'country',
        'region',
        'city',
        'state',
        'postal_code'
    ]].drop_duplicates()

    return customers
from sqlalchemy import create_engine

def create_fact_orders(df):
    print("Creating fact_orders table...")

    fact_orders = df[[
        'order_id',
        'customer_id',
        'product_id',
        'order_date',
        'ship_date',
        'sales',
        'quantity',
        'discount',
        'profit'
    ]].copy()

    return fact_orders


# 4. Save to SQLite
def load_to_sqlite(df, table_name, db_name="data/retail_data.db"):
    print(f"Saving {table_name} to SQLite...")
    engine = create_engine(f"sqlite:///{db_name}")
    df.to_sql(table_name, con=engine, index=False, if_exists='replace')

# Main ETL runner
def run_etl():
    raw_path = "data/raw/superstore.csv"
    df = extract_data(raw_path)
    df = clean_column_names(df)

    print(df.head())

    # Create and save dim_customers
    dim_customers = create_dim_customers(df)
    print(dim_customers.head())
    load_to_sqlite(dim_customers, table_name="dim_customers")

    # Create and save fact_orders
    fact_orders = create_fact_orders(df)
    print(fact_orders.head())
    load_to_sqlite(fact_orders, table_name="fact_orders")


if __name__ == "__main__":
    run_etl()

