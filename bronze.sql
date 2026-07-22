-- Databricks notebook source
CREATE SCHEMA IF NOT EXISTS bronze;

CREATE OR REPLACE TABLE bronze.bookings AS
SELECT * FROM samples.wanderbricks.bookings;

CREATE OR REPLACE TABLE bronze.properties AS
SELECT * FROM samples.wanderbricks.properties;

CREATE OR REPLACE TABLE bronze.destinations AS
SELECT * FROM samples.wanderbricks.destinations;

-- COMMAND ----------

SELECT 
    b.*,
    p.*,
    d.*
FROM bronze.bookings b
LEFT JOIN bronze.properties p ON b.property_id = p.property_id
LEFT JOIN bronze.destinations d ON p.destination_id = d.destination_id
WHERE d.country = 'Japan' 
  AND status IN ('confirmed', 'completed');