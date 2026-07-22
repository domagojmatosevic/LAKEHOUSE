# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS bronze;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE bronze.bookings AS
# MAGIC SELECT * FROM samples.wanderbricks.bookings;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE bronze.properties AS
# MAGIC SELECT * FROM samples.wanderbricks.properties;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE bronze.destinations AS
# MAGIC SELECT * FROM samples.wanderbricks.destinations;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     b.*,
# MAGIC     p.*,
# MAGIC     d.*
# MAGIC FROM bronze.bookings b
# MAGIC LEFT JOIN bronze.properties p ON b.property_id = p.property_id
# MAGIC LEFT JOIN bronze.destinations d ON p.destination_id = d.destination_id
# MAGIC WHERE d.country = 'Japan' 
# MAGIC   AND status IN ('confirmed', 'completed');