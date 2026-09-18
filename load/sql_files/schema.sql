

CREATE TABLE IF NOT EXISTS cities (
    city_id  SERIAL PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    latitude DOUBLE PRECISION NOT NULL,
    longitude DOUBLE PRECISION NOT NULL,
    UNIQUE(city)
);


CREATE TABLE IF NOT EXISTS  forecasts (
    forecast_id SERIAL PRIMARY KEY,

    city_id INTEGER NOT NULL,
    date DATE NOT NULL,

    temp_max DOUBLE PRECISION,
    temp_min DOUBLE PRECISION,
    precipitation DOUBLE PRECISION,
    precipitation_probability INTEGER,
    wind_speed_max DOUBLE PRECISION,
    wind_gust_max DOUBLE PRECISION,
    weather_code INTEGER,

    weather_category VARCHAR(50),
    rain_category VARCHAR(50),
    temp_max_category VARCHAR(50),
    temp_min_category VARCHAR(50),
    wind_category VARCHAR(50),

    rain_score DOUBLE PRECISION,
    temp_max_score DOUBLE PRECISION,
    temp_min_score DOUBLE PRECISION,
    wind_score DOUBLE PRECISION,

    risk DOUBLE PRECISION,
    risk_level VARCHAR(30),

    FOREIGN KEY (city_id) REFERENCES cities(city_id),

    UNIQUE(city_id, date)
);