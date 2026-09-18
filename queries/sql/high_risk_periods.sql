-- Query 2: High-risk forecast periods
SELECT
    c.city,
    f.date,
    f.risk,
    f.risk_level,
    f.precipitation,
    f.precipitation_probability,
    f.wind_speed_max,
    f.wind_gust_max
FROM forecasts f
JOIN cities c
    ON f.city_id = c.city_id
WHERE f.risk_level in ('high', 'very high', 'extremely high')
ORDER BY f.risk DESC, f.date;