# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS silver;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE silver.japan_bookings_2024 AS
# MAGIC SELECT
# MAGIC     b.booking_id,
# MAGIC     b.property_id,
# MAGIC     b.check_in,
# MAGIC     b.check_out,
# MAGIC     b.guests_count,
# MAGIC     b.total_amount,
# MAGIC     b.status,
# MAGIC     p.base_price,
# MAGIC     p.max_guests,
# MAGIC     p.property_latitude AS latitude,
# MAGIC     p.property_longitude AS longitude,
# MAGIC     d.destination AS city
# MAGIC FROM bronze.bookings b
# MAGIC JOIN bronze.properties p ON b.property_id = p.property_id
# MAGIC JOIN bronze.destinations d ON p.destination_id = d.destination_id
# MAGIC WHERE d.country = 'Japan'
# MAGIC   AND YEAR(b.check_in) = 2024
# MAGIC   AND b.status IN ('confirmed', 'completed')
# MAGIC   AND b.total_amount IS NOT NULL
# MAGIC   AND b.check_in IS NOT NULL
# MAGIC   AND b.check_out IS NOT NULL;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM silver.japan_bookings_2025