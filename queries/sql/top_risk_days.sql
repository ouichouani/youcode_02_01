-- Bonus: Top 3 riskiest days for each city
WITH ranked_forecasts AS (
    SELECT
        c.city,
        f.date,
        f.risk,
        f.risk_level,
        ROW_NUMBER() OVER (
            PARTITION BY c.city
            ORDER BY f.risk DESC
        ) AS risk_rank
    FROM forecasts f
    JOIN cities c
        ON f.city_id = c.city_id
)
SELECT
    city,
    date,
    risk,
    risk_level,
    risk_rank
FROM ranked_forecasts
WHERE risk_rank <= 3
ORDER BY city, risk_rank;