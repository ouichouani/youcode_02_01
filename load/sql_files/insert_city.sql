
INSERT INTO cities (city, latitude, longitude)
VALUES (%s, %s, %s)
ON CONFLICT (city) DO NOTHING;