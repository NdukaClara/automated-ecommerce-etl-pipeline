# 🛒 Automated E-Commerce ETL Pipeline  

## 📌 Project Overview  
This project demonstrates a modern **end-to-end data engineering pipeline** built with:  

- ✅ **Python** — for generating dummy e-commerce data (customers, orders, shipments).  
- ✅ **Snowflake** — as the cloud data warehouse.  
- ✅ **dbt** — for transformations (raw → analytics).  
- ✅ **Apache Airflow** — for orchestration and scheduling.  

The pipeline simulates an **E-commerce order monitoring system**, taking raw data through ingestion, transformation, and analytics-ready modeling.  

---

## 🏗️ Architecture  
1. **Data Generation**: Python scripts create synthetic e-commerce datasets (CSV format).  
2. **Raw Layer**: Data is loaded into a `raw` schema in Snowflake.  
3. **Transformations**: dbt models clean, join, and structure the data into fact & dimension tables.  
4. **Analytics Layer**: Results are materialized into an `analytics` schema.  
5. **Orchestration**: Airflow DAG schedules the pipeline.  

---

## ⚙️ Tech Stack  
- **Language**: Python 3.9  
- **Warehouse**: Snowflake  
- **Transformations**: dbt  
- **Orchestration**: Apache Airflow  
- **Version Control**: GitHub  

---

## 🚀 Setup & Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/NdukaClara/automated-ecommerce-etl-pipeline.git
cd automated-ecommerce-etl-pipeline
