-- Query 1: Average risk by city
SELECT
    c.city,
    ROUND(AVG(f.risk)::numeric, 2) AS average_risk,
    MAX(f.risk) AS maximum_risk
FROM forecasts f
JOIN cities c
    ON f.city_id = c.city_id
GROUP BY c.city
ORDER BY average_risk DESC;