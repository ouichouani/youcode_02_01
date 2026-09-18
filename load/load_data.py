from load.connection import get_connection
from transformation.gold import gold_data


connection = get_connection()
cursor = connection.cursor()

def insert_cities(cursor):
    cities = gold_data[
        ["city", "latitude", "longitude"]
    ].drop_duplicates()

    with open ("load/sql_files/insert_city.sql", "r") as file:
        insert_city_query = file.read()


    for _, row in cities.iterrows():
        cursor.execute(insert_city_query , (row["city"], row["latitude"], row["longitude"]))

    connection.commit()
    print("Cities loaded successfully!")

def get_cities(cursor):
    cursor.execute("SELECT city , city_id FROM cities")
    cities = cursor.fetchall()
    return dict(cities)

def add_city_id(cursor):
    # add city_id to gold_data
    gold_data["city_id"] = gold_data["city"].map(get_cities(cursor))

def insert_forecasts(cursor):

    columns = [
        "city_id",
        "date",
        "temp_max",
        "temp_min",
        "precipitation",
        "precipitation_probability",
        "wind_speed_max",
        "wind_gust_max",
        "weather_code",
        "weather_category",
        "rain_category",
        "temp_max_category",
        "temp_min_category",
        "wind_category",
        "rain_score",
        "temp_max_score",
        "temp_min_score",
        "wind_score",
        "risk",
        "risk_level"
    ]

    if gold_data["city_id"].isna().sum() > 0:
        print("Some cities are missing city_id. Please check the data.")
        return
    
    with open("load/sql_files/insert_forecasts.sql", "r") as file:
        insert_forecast_query = file.read()

    for _,row in gold_data.iterrows():
        values = tuple(row[column] for column in columns)
        cursor.execute(insert_forecast_query, values)
        
    connection.commit()
    print("Forecasts loaded successfully!")

add_city_id(cursor)
insert_forecasts(cursor)

cursor.close()
connection.close()



# 