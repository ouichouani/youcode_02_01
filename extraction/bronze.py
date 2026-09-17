
import pandas as pd
import requests as rq
import json
import os

worldcities = pd.read_csv("worldcities.csv")
morocco = worldcities.loc[worldcities["country"] == "Morocco"].copy()


def get_api_data( latitude , longitude) :
    try :
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": [
                "temperature_2m_max",
                "temperature_2m_min",
                "precipitation_sum",
                "precipitation_probability_max",
                "wind_speed_10m_max",
                "wind_gusts_10m_max",
                "weather_code"
            ],
            "forecast_days": 7
        }

        response = rq.get(url , params=params , timeout=10)
        response.raise_for_status()
        return response.json()

    except rq.exceptions.Timeout:
        print("Request timed out")
        return None

    except rq.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None

    except ValueError:
        print("Invalid JSON response")
        return None

def store_bronze(file_name , data) :
    try :
        if not os.path.exists("bronze/"):
            os.makedirs("bronze")

        with open(file_name , 'w') as file:
            json.dump(data , file , indent=4)
    except OSError as e:
        print(f"Error storing data: {e}")

def get_all_cities_data():
    for  _, city in morocco.iterrows():
        print(city["city"])
        city_name = city['city']
        latitude = city['lat']
        longitude = city['lng']

        data = get_api_data( latitude , longitude )

        if not data : 
            raise("Error fetching data for city: {city_name}")

        file_name = "bronz/" + city_name + ".json"
        store_bronze(file_name , data)
        print(f"Data for {city_name} stored successfully")
