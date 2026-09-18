-- Query 5: Extreme temperature conditions
SELECT
    c.city,
    f.date,
    f.temp_min,
    f.temp_max,
    f.temp_min_category,
    f.temp_max_category,
    f.risk,
    f.risk_level
FROM forecasts f
JOIN cities c
    ON f.city_id = c.city_id
WHERE f.temp_min_category IN ('very hot')
   OR f.temp_max_category IN ('very hot')
ORDER BY f.risk DESC;
