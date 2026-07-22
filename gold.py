# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS gold;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE gold.monthly_price_trends AS
# MAGIC SELECT
# MAGIC     city,
# MAGIC     YEAR(check_in) AS year,
# MAGIC     MONTH(check_in) AS month,
# MAGIC     ROUND(AVG(total_amount / NULLIF(DATEDIFF(check_out, check_in), 0)), 2) AS avg_price,
# MAGIC     ROUND(MIN(total_amount / NULLIF(DATEDIFF(check_out, check_in), 0)), 2) AS min_price,
# MAGIC     ROUND(MAX(total_amount / NULLIF(DATEDIFF(check_out, check_in), 0)), 2) AS max_price,
# MAGIC     COUNT(*) AS booking_count,
# MAGIC     SUM(DATEDIFF(check_out, check_in)) AS total_nights
# MAGIC FROM silver.japan_bookings_2024
# MAGIC GROUP BY city, YEAR(check_in), MONTH(check_in)
# MAGIC ORDER BY city, year, month;
# MAGIC
# MAGIC CREATE OR REPLACE TABLE gold.geo_price_index AS
# MAGIC SELECT
# MAGIC     property_id,
# MAGIC     city,
# MAGIC     YEAR(check_in) AS year,
# MAGIC     MONTH(check_in) AS month,
# MAGIC     ROUND(AVG(total_amount / NULLIF(DATEDIFF(check_out, check_in), 0)), 2) AS avg_price,
# MAGIC     ROUND(MIN(total_amount / NULLIF(DATEDIFF(check_out, check_in), 0)), 2) AS min_price,
# MAGIC     ROUND(MAX(total_amount / NULLIF(DATEDIFF(check_out, check_in), 0)), 2) AS max_price,
# MAGIC     latitude,
# MAGIC     longitude
# MAGIC FROM silver.japan_bookings_2024
# MAGIC GROUP BY property_id, city, YEAR(check_in), MONTH(check_in), latitude, longitude
# MAGIC ORDER BY city, year, month;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM gold.monthly_price_trends