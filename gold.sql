-- Databricks notebook source

CREATE SCHEMA IF NOT EXISTS gold;

CREATE OR REPLACE TABLE gold.monthly_price_trends AS
SELECT
    city,
    YEAR(check_in) AS year,
    MONTH(check_in) AS month,
    ROUND(AVG(total_amount / NULLIF(DATEDIFF(check_out, check_in), 0)), 2) AS avg_price,
    ROUND(MIN(total_amount / NULLIF(DATEDIFF(check_out, check_in), 0)), 2) AS min_price,
    ROUND(MAX(total_amount / NULLIF(DATEDIFF(check_out, check_in), 0)), 2) AS max_price,
    COUNT(*) AS booking_count,
    SUM(DATEDIFF(check_out, check_in)) AS total_nights
FROM silver.japan_bookings_2024
GROUP BY city, YEAR(check_in), MONTH(check_in)
ORDER BY city, year, month;

CREATE OR REPLACE TABLE gold.geo_price_index AS
SELECT
    property_id,
    city,
    YEAR(check_in) AS year,
    MONTH(check_in) AS month,
    ROUND(AVG(total_amount / NULLIF(DATEDIFF(check_out, check_in), 0)), 2) AS avg_price,
    ROUND(MIN(total_amount / NULLIF(DATEDIFF(check_out, check_in), 0)), 2) AS min_price,
    ROUND(MAX(total_amount / NULLIF(DATEDIFF(check_out, check_in), 0)), 2) AS max_price,
    latitude,
    longitude
FROM silver.japan_bookings_2024
GROUP BY property_id, city, YEAR(check_in), MONTH(check_in), latitude, longitude
ORDER BY city, year, month;

-- COMMAND ----------


SELECT * FROM gold.monthly_price_trends