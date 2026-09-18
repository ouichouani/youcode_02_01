
from load.connection import get_connection


def execute_query(sql_file):

    connection = get_connection()
    cursor = connection.cursor()

    with open(sql_file, "r") as file:
        query = file.read()

    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


def get_highest_risk_cities():
    return execute_query("queries/sql/highest_risk_cities.sql")


def get_high_risk_periods():
    return execute_query("queries/sql/high_risk_periods.sql")


def get_heavy_rain_cities():
    return execute_query("queries/sql/heavy_rain.sql")


def get_strong_wind_conditions():
    return execute_query("queries/sql/strong_wind.sql")


def get_extreme_temperature():
    return execute_query("queries/sql/extreme_temperature.sql")


def get_top_risk_days():
    return execute_query("queries/sql/top_risk_days.sql")


def city_number() :
    return execute_query("queries/sql/KPI_number_of_cities.sql")

def get_map_data():
    return execute_query("queries/sql/map_data.sql")


# result = get_highest_risk_cities()
# for row in result:
#     print(row)


# result = get_high_risk_periods()
# for row in result:
#     print(row)


# result = get_heavy_rain_cities()
# for row in result:
#     print(row)


# result = get_strong_wind_conditions()
# for row in result:
#     print(row)


# result = get_extreme_temperature()
# for row in result:
#     print(row)

# result = get_top_risk_days()
# for row in result:
#     print(row)