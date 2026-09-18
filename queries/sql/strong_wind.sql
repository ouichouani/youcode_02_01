-- Query 4: Strongest wind conditions
SELECT
    c.city,
    f.date,
    f.wind_speed_max,
    f.wind_gust_max,
    f.risk,
    f.risk_level
FROM forecasts f
JOIN cities c
    ON f.city_id = c.city_id
WHERE f.wind_speed_max >= 30
ORDER BY f.wind_speed_max DESC;