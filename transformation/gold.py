
import pandas as pd
from transformation.silver import silver_data


def category_system(gold_data) :

    gold_data["rain_category"] = pd.cut(
        gold_data["precipitation"],
        bins=[-1, 0, 5, 20, 50, float("inf")],
        labels=[ "no rain", "light rain", "moderate rain", "heavy rain", "extreme rain" ]
    )

    gold_data["temp_max_category"] = pd.cut(
        gold_data["temp_max"] ,
        bins=[-float("inf"), 10, 20, 30, 45, float("inf")],
        labels = ["very cold" , "cold" , "normal" , "hot" , "very hot"]
    )

    gold_data["temp_min_category"] = pd.cut(
        gold_data["temp_min"] ,
        bins=[-float("inf"), 10, 20, 30, 45, float("inf")],
        labels = ["very cold" , "cold" , "normal" , "hot" , "very hot"]
    )

    gold_data["wind_category"] = pd.cut(
        gold_data["wind_speed_max"] ,
        bins=[-float("inf"), 10, 20, 30, 45, float("inf")],
        labels = ["no wind" , "light wind" , "moderate wind" , "strong wind" , "very strong wind"]
    )

    weather_mapping = {
        0: "Clear",
        1: "Cloudy",
        2: "Cloudy",
        3: "Cloudy",
        45: "Fog",
        48: "Fog",
        51: "Drizzle",
        53: "Drizzle",
        55: "Drizzle",
        61: "Rain",
        63: "Rain",
        65: "Heavy rain",
        71: "Snow",
        73: "Snow",
        75: "Heavy snow",
        80: "Rain showers",
        81: "Rain showers",
        82: "Heavy rain showers",
        95: "Thunderstorm",
        96: "Thunderstorm",
        99: "Thunderstorm"
    }

    gold_data["weather_category"] = gold_data["weather_code"].map(
        weather_mapping
    )

    return gold_data

def risk_system(gold_data):

    gold_data["wind_score"] = gold_data["wind_category"].map({
        "no wind": 0,
        "light wind": 5,
        "moderate wind": 10,
        "strong wind": 15,
        "very strong wind": 20
    })

    gold_data["temp_max_score"] = gold_data["temp_max_category"].map({
        "very cold": 20,
        "cold": 7,
        "normal": 0,
        "hot": 7,
        "very hot": 20
    })

    gold_data["temp_min_score"] = gold_data["temp_min_category"].map({
        "very cold": 20,
        "cold": 7,
        "normal": 0,
        "hot": 7,
        "very hot": 20
    })

    gold_data["rain_score"] = gold_data["rain_category"].map({
        "no rain": 0,
        "light rain": 10,
        "moderate rain": 20,
        "heavy rain": 30,
        "extreme rain": 40
    })

    gold_data["wind_score"] = pd.to_numeric(gold_data["wind_score"], errors='coerce')
    gold_data["temp_min_score"] = pd.to_numeric(gold_data["temp_min_score"], errors='coerce')
    gold_data["temp_max_score"] = pd.to_numeric(gold_data["temp_max_score"], errors='coerce')
    gold_data["rain_score"] = pd.to_numeric(gold_data["rain_score"], errors='coerce')
    

    gold_data["risk"] = ((gold_data["rain_score"] * (gold_data["precipitation_probability"] / 100) ) + gold_data["temp_min_score"] + gold_data["temp_max_score"] + gold_data["wind_score"])
    return gold_data

def risk_level(gold_data) :

    gold_data["risk_level"] = pd.cut(
        gold_data["risk"],
        bins = [-1 , 15, 25 , 50 , 75 , 100] ,
        labels = ["low", "medium", "high", "very high", "extremely high"]
    )

    return gold_data

def quality_check(gold_data) :
    score_columns = [
        "rain_score",
        "temp_min_score",
        "temp_max_score",
        "wind_score",
        "risk" ,
        "risk_level"
    ]

    null_values_count = gold_data[score_columns].isna().sum()

    print('risk value count'.center(80 , '-'))
    print(gold_data["risk_level"].value_counts())

    print("Missing values in score columns".center(80 , '-'))
    print(null_values_count)

    print(f"Minimum risk: {gold_data['risk'].min()}")
    print(f"Maximum risk: {gold_data['risk'].max()}")

    if not gold_data["risk"].between(0, 100).all():
        print("Risk score outside 0-100 range")
    else:
        print("Risk scores are within 0-100")

gold_data = silver_data.copy()
gold_data = category_system(gold_data)
gold_data = risk_system(gold_data)
gold_data = risk_level(gold_data)

if __name__ == "__main__":
    quality_check(gold_data)





