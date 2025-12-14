# 🛍️ Retail Sales ETL Pipeline

This is a simple data engineering project that extracts, transforms, and loads (ETL) retail sales data from a CSV file into a star-schema SQLite database using Python.

## 🧠 What It Shows
- ✅ Python-based ETL design
- ✅ Data cleaning with pandas
- ✅ Dimensional modeling (fact + dimension tables)
- ✅ SQLite database integration using SQLAlchemy
- ✅ GitHub project structure + CLI pipeline

## 📁 Project Structure

retail-sales-etl-pipeline/
│
├── data/
│ └── raw/ # Raw CSV data
│ └── retail_data.db # SQLite DB (ignored in .gitignore)
│
├── scripts/ # Python ETL scripts
│ └── etl_pipeline.py # Main ETL runner
│
├── notebooks/ # Optional analysis notebooks
├── models/ # Schema diagrams or model definitions
├── .gitignore
├── README.md


## 🗃️ Data Tables Created

| Table Name       | Description                   |
|------------------|-------------------------------|
| `dim_customers`  | Unique customer info          |
| `dim_products`   | Product details and categories|
| `dim_regions`    | Location and postal info      |
| `fact_orders`    | Transaction-level sales facts |

## ▶️ How to Run

In terminal:

```bash
python3 scripts/etl_pipeline.py
