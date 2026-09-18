
import streamlit as st
import pandas as pd

from queries.queries import (
    get_highest_risk_cities,
    city_number,
    get_high_risk_periods,
    get_heavy_rain_cities,
    get_strong_wind_conditions,
    get_extreme_temperature,
    get_top_risk_days
)


# PAGE CONFIGURATION

st.set_page_config(
    page_title="Morocco Weather Dashboard",
    page_icon="🌥️",
    layout="wide"
)


# TITLE

st.title("Morocco Weather Dashboard 🌥️")

st.write(
    "Weather risk monitoring for Moroccan cities."
)


# LOAD DATA

highest_risk_cities = pd.DataFrame(
    get_highest_risk_cities(),
    columns=["city", "average_risk", "maximum_risk"]
)

high_risk_periods = pd.DataFrame(
    get_high_risk_periods(),
    columns=[
        "city",
        "date",
        "risk",
        "risk_level",
        "precipitation",
        "precipitation_probability",
        "wind_speed_max",
        "wind_gust_max"
    ]
)

heavy_rain = pd.DataFrame(
    get_heavy_rain_cities(),
    columns=[
        "city",
        "rainy_days",
        "average_precipitation",
        "maximum_precipitation"
    ]
)

strong_wind = pd.DataFrame(
    get_strong_wind_conditions(),
    columns=[
        "city",
        "date",
        "wind_speed_max",
        "wind_gust_max",
        "risk",
        "risk_level"
    ]
)

extreme_temperature = pd.DataFrame(
    get_extreme_temperature(),
    columns=[
        "city",
        "date",
        "temp_min",
        "temp_max",
        "temp_min_category",
        "temp_max_category",
        "risk",
        "risk_level"
    ]
)

top_risk_days = pd.DataFrame(
    get_top_risk_days(),
    columns=[
        "city",
        "date",
        "risk",
        "risk_level",
        "risk_rank"
    ]
)


# KPI SECTION

st.header("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Number of Cities",
        city_number()[0][0]
    )

with col2:
    st.metric(
        "Maximum Temperature",
        f"{extreme_temperature['temp_max'].max()} °C"
    )

with col3:
    st.metric(
        "Maximum Precipitation",
        f"{heavy_rain['maximum_precipitation'].max()} mm"
    )

with col4:
    st.metric(
        "High-Risk Periods",
        len(high_risk_periods)
    )


# HIGHEST RISK CITIES

st.header("Highest Risk Cities")

st.dataframe(
    highest_risk_cities,
    use_container_width=True
)


# HIGH-RISK PERIODS

st.header("High-Risk Forecast Periods")

st.dataframe(
    high_risk_periods,
    use_container_width=True
)


# HEAVY RAIN

st.header("Heavy Rain Conditions")

st.dataframe(
    heavy_rain,
    use_container_width=True
)


# STRONG WIND

st.header("Strong Wind Conditions")

st.dataframe(
    strong_wind,
    use_container_width=True
)


# EXTREME TEMPERATURE

st.header("Extreme Temperature Conditions")

st.dataframe(
    extreme_temperature,
    use_container_width=True
)


# TOP RISK DAYS

st.header("Top Risk Days")

st.dataframe(
    top_risk_days,
    use_container_width=True
)