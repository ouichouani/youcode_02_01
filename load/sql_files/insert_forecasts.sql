INSERT INTO forecasts (
city_id ,
date ,
temp_max ,
temp_min ,
precipitation ,
precipitation_probability ,
wind_speed_max ,
wind_gust_max ,
weather_code ,
weather_category ,
rain_category ,
temp_max_category ,
temp_min_category ,
wind_category ,
rain_score ,
temp_max_score ,
temp_min_score ,
wind_score ,
risk ,
risk_level 
)
VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)
ON CONFLICT (date , city_id)
DO UPDATE SET
    temp_max = EXCLUDED.temp_max,
    temp_min = EXCLUDED.temp_min,
    precipitation = EXCLUDED.precipitation,
    precipitation_probability = EXCLUDED.precipitation_probability,
    wind_speed_max = EXCLUDED.wind_speed_max,
    wind_gust_max = EXCLUDED.wind_gust_max,
    weather_code = EXCLUDED.weather_code,
    weather_category = EXCLUDED.weather_category,
    rain_category = EXCLUDED.rain_category,
    temp_max_category = EXCLUDED.temp_max_category,
    temp_min_category = EXCLUDED.temp_min_category,
    wind_category = EXCLUDED.wind_category,
    rain_score = EXCLUDED.rain_score,
    temp_max_score = EXCLUDED.temp_max_score,
    temp_min_score = EXCLUDED.temp_min_score,
    wind_score = EXCLUDED.wind_score,
    risk = EXCLUDED.risk,
    risk_level = EXCLUDED.risk_level;


