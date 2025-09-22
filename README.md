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
```

### 2️⃣ Create a Virtual Environment
```bash
python3 -m venv airflow_venv_1
source airflow_venv_1/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure dbt (Snowflake Profile)

Edit your ~/.dbt/profiles.yml with Snowflake credentials:
```yaml
ecommerce_project:
  target: dev
  outputs:
    dev:
      type: snowflake
      account: <account>
      user: <user>
      password: <password>
      role: <role>
      database: ecommerce_db
      warehouse: <warehouse>
      schema: raw
```

### 5️⃣ Run dbt Models
```bash
dbt run
```

### 6️⃣ Run Airflow (Standalone Mode for Dev)
```bash
airflow standalone
```

## 📊 Example dbt Models

stg_orders → staging table

dim_customers → dimension table

fct_orders → fact table

## 📝 Project Structure
```plaintext
ecommerce_etl_project/
│── dags/                # Airflow DAGs  
│── dbt/                 # dbt models  
│── data/                # Generated CSVs  
│── scripts/             # Python data generator  
│── airflow_venv_1/      # Virtual environment (excluded in .gitignore)  
│── requirements.txt     # Dependencies  
│── README.md            # Project documentation  
```

## 🔮 Future Improvements

Add monitoring with Great Expectations

Add dbt tests for data quality

Deploy Airflow with Docker Compose

## 🙌 Acknowledgments

This project was built as part of my journey into Data Engineering, focusing on practical, real-world pipelines.
