-- snowflake/setup_snowflake.sql

-- Create warehouse
CREATE WAREHOUSE IF NOT EXISTS ecommerce_wh
  WITH WAREHOUSE_SIZE = 'XSMALL'
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE;

  -- Create database
CREATE DATABASE IF NOT EXISTS ecommerce_db;
USE DATABASE ecommerce_db;

-- Create schemas
CREATE SCHEMA IF NOT EXISTS ecommerce_db.raw;
CREATE SCHEMA IF NOT EXISTS ecommerce_db.analytics;

-- Raw Tables
CREATE OR REPLACE TABLE raw.orders (
    order_id STRING,
    customer_id STRING,
    order_date DATE
);

CREATE OR REPLACE TABLE raw.shipments (
    shipment_id STRING,
    order_id STRING,
    status STRING,
    shipped_at TIMESTAMP,
    delivered_at TIMESTAMP
);

CREATE OR REPLACE TABLE raw.customers (
    customer_id STRING,
    name STRING,
    email STRING
);

select * from raw.orders

select * from ECOMMERCE_DB.ANALYTICS.ORDER_STATUS

select * from ECOMMERCE_DB.RAW.SHIPMENTS

update ECOMMERCE_DB.RAW.SHIPMENTS 
set delivered_at = '2024-01-05' &  where shipment_id = 'S1'

update ECOMMERCE_DB.RAW.SHIPMENTS 
set status = 'shipped' where shipment_id = 'S1'

update ECOMMERCE_DB.RAW.SHIPMENTS 
set delivered_at = '2024-01-13' where shipment_id = 'S8'