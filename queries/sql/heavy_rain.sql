-- Query 3: Cities with heavy or extreme rain
SELECT
    c.city,
    COUNT(*) AS rainy_days,
    ROUND(AVG(f.precipitation)::numeric, 2) AS average_precipitation,
    MAX(f.precipitation) AS maximum_precipitation
FROM forecasts f
JOIN cities c
    ON f.city_id = c.city_id
WHERE f.rain_category IN ('heavy rain', 'extreme rain')
GROUP BY c.city
ORDER BY maximum_precipitation DESC;