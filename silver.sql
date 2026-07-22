-- Databricks notebook source
CREATE SCHEMA IF NOT EXISTS silver;

CREATE OR REPLACE TABLE silver.japan_bookings_2024 AS
SELECT
    b.booking_id,
    b.property_id,
    b.check_in,
    b.check_out,
    b.guests_count,
    b.total_amount,
    b.status,
    p.base_price,
    p.max_guests,
    p.property_latitude AS latitude,
    p.property_longitude AS longitude,
    d.destination AS city
FROM bronze.bookings b
JOIN bronze.properties p ON b.property_id = p.property_id
JOIN bronze.destinations d ON p.destination_id = d.destination_id
WHERE d.country = 'Japan'
  AND YEAR(b.check_in) = 2024
  AND b.status IN ('confirmed', 'completed')
  AND b.total_amount IS NOT NULL
  AND b.check_in IS NOT NULL
  AND b.check_out IS NOT NULL;

-- COMMAND ----------

SELECT * FROM silver.japan_bookings_2024
