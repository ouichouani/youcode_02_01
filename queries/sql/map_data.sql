SELECT
    c.city,
    c.latitude,
    c.longitude,
    f.date,
    f.risk,
    f.risk_level
FROM forecasts f
JOIN cities c
    ON f.city_id = c.city_id
ORDER BY f.date, f.risk DESC;