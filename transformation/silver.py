import pandas as pd
import json
import os
from pathlib import Path

def read_bronze_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            
            if not isinstance(data , dict):
                print(f"Invalid data format in {file_name}")
                return None
            
            return data
    except OSError as e :
        print(f"Error reading data: {e}")

def read_all_files(silver_data):

    # check absolut path from the current working directory
    folder = Path("extraction/bronze/")
    if(not folder.exists()):
        print(f"Folder does not exist in \"{folder}\"")
        # check relative path
        folder = Path("../extraction/bronze/")
        if(not folder.exists()):
            print(f"Folder does not exist in \"{folder}\"")
            return None

    

    files = list(folder.glob("*.json"))
    for file in files:

        if not file.is_file() :
            print(f"Invalid file: {file}")
            continue
        data = read_bronze_file(file)
        if data is None: continue

        daily = data["daily"]
        df = pd.DataFrame(daily)
        df['city'] = file.stem
        df["latitude"] = data["latitude"]
        df["longitude"] = data["longitude"]

        silver_data = pd.concat([silver_data ,  df ] , ignore_index=True)
        print(f"file {file} read successfully")
        


    os.system("cls")
    print("All files read successfully")
    return silver_data

def transform_data(silver_data) :    
    silver_data['date'] = pd.to_datetime(silver_data['date'])
    silver_data = silver_data.drop_duplicates(subset=["city", "date"],ignore_index=True)
    return silver_data

def validate_data(silver_data):
    print('from transform_data function'.center(50 , "-"))

    print("Missing values:")
    print(silver_data.isna().sum())

    print("Duplicate city/date:", 
          silver_data.duplicated(["city", "date"]).sum())

    print("Probability valid:",
          silver_data["precipitation_probability"].between(0, 100).all())

    print("Temperatures consistent:",
          (silver_data["temp_max"] >= silver_data["temp_min"]).all())

    print("Negative precipitation:",
          (silver_data["precipitation"] < 0).sum())

    print("Negative wind speed:",
          (silver_data["wind_speed_max"] < 0).sum())
    
    print('-'.center(50 , "-"))

def rename_column(silver_data) : 
    return silver_data.rename(columns= {
        "time": "date",
        "temperature_2m_max": "temp_max",
        "temperature_2m_min": "temp_min",
        "precipitation_sum": "precipitation",
        "precipitation_probability_max": "precipitation_probability",
        "wind_speed_10m_max": "wind_speed_max",
        "wind_gusts_10m_max": "wind_gust_max",
        "weather_code": "weather_code"
    })


silver_data = pd.DataFrame()
silver_data = read_all_files(silver_data)

if silver_data is None : 
    print("No data found , check silver file , Exiting program ...")
    exit(1)

silver_data = rename_column(silver_data)
silver_data = transform_data(silver_data)

if __name__ == "__main__":
    validate_data(silver_data)





