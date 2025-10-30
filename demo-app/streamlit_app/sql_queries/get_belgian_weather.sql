  -- This file contains the SQL logic to fetch Belgian weather data.
WITH
  WEATHER_DATA AS (
  SELECT
    stn,
    -- Convert string date to actual DATE object
    PARSE_DATE('%Y%m%d', CONCAT(year, mo, da)) AS date,
    -- Handle missing data flags (9999.9 or 99.99)
    -- Temperatures in Fahrenheit for now
    NULLIF(TEMP, 9999.9) AS avg_temp_f,
    NULLIF(max, 9999.9) AS max_temp_f,
    NULLIF(min, 9999.9) AS min_temp_f
  FROM
    `bigquery-public-data.noaa_gsod.gsod2025` ),
  BELGIAN_STATION_DATA AS (
  SELECT
    usaf,
    name,
    lat,
    lon
  FROM
    `bigquery-public-data.noaa_gsod.stations`
  WHERE
    -- Only focus on Belgian weather data
    country = 'BE' )
SELECT
  B.name AS station_name,
  W.date,
  -- Convert to easier to understand metrics (Celsius, millimeter and kilometer per hour)
  ROUND((W.avg_temp_f - 32) * 5 / 9, 1) AS avg_temp_celsius,
  ROUND((W.min_temp_f - 32) * 5 / 9, 1) AS min_temp_celsius,
  ROUND((W.max_temp_f - 32) * 5 / 9, 1) AS max_temp_celsius,
  B.lat,
  B.lon
FROM
  WEATHER_DATA AS W
INNER JOIN
  BELGIAN_STATION_DATA AS B
ON
  W.stn = B.usaf
WHERE
  -- Remove days where no temperature measurements are available
  W.avg_temp_f IS NOT NULL
ORDER BY
  B.name,
  W.date;