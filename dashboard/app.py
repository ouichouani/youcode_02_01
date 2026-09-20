
# import streamlit as st
# import pandas as pd

# from queries.queries import (
#     get_highest_risk_cities,
#     city_number,
#     get_high_risk_periods,
#     get_heavy_rain_cities,
#     get_strong_wind_conditions,
#     get_extreme_temperature,
#     get_top_risk_days ,
#     get_map_data
# )


# # PAGE CONFIGURATION

# st.set_page_config(
#     page_title="Morocco Weather Dashboard",
#     page_icon="🌥️",
#     layout="wide"
# )


# sidebar , main = st.columns(2)

# with sidebar:
#     st.title("Dashboard Sidebar")
#     st.write("Explore Morocco's weather risk data.")
#     st.write("Select a section to view")

# with main :
#     st.title("Morocco Weather Dashboard 🌥️")
#     st.write("Weather risk monitoring for Moroccan cities.")


#     # LOAD DATA

#     highest_risk_cities = pd.DataFrame(
#         get_highest_risk_cities(),
#         columns=["city", "average_risk", "maximum_risk"]
#     )

#     high_risk_periods = pd.DataFrame(
#         get_high_risk_periods(),
#         columns=[
#             "city",
#             "date",
#             "risk",
#             "risk_level",
#             "precipitation",
#             "precipitation_probability",
#             "wind_speed_max",
#             "wind_gust_max"
#         ]
#     )

#     heavy_rain = pd.DataFrame(
#         get_heavy_rain_cities(),
#         columns=[
#             "city",
#             "rainy_days",
#             "average_precipitation",
#             "maximum_precipitation"
#         ]
#     )

#     strong_wind = pd.DataFrame(
#         get_strong_wind_conditions(),
#         columns=[
#             "city",
#             "date",
#             "wind_speed_max",
#             "wind_gust_max",
#             "risk",
#             "risk_level"
#         ]
#     )

#     extreme_temperature = pd.DataFrame(
#         get_extreme_temperature(),
#         columns=[
#             "city",
#             "date",
#             "temp_min",
#             "temp_max",
#             "temp_min_category",
#             "temp_max_category",
#             "risk",
#             "risk_level"
#         ]
#     )

#     top_risk_days = pd.DataFrame(
#         get_top_risk_days(),
#         columns=[
#             "city",
#             "date",
#             "risk",
#             "risk_level",
#             "risk_rank"
#         ]
#     )


#     # KPI SECTION

#     st.header("Key Performance Indicators")
#     col1, col2, col3, col4 = st.columns(4)

#     with col1:
#         st.metric(
#             "Number of Cities",
#             city_number()[0][0]
#         )

#     with col2:
#         st.metric(
#             "Maximum Temperature",
#             f"{extreme_temperature['temp_max'].max()} °C"
#         )

#     with col3:
#         st.metric(
#             "Maximum Precipitation",
#             f"{heavy_rain['maximum_precipitation'].max()} mm"
#         )

#     with col4:
#         st.metric(
#             "High-Risk Periods",
#             len(high_risk_periods)
#         )


#     # # HIGHEST RISK CITIES

#     # st.header("Highest Risk Cities")

#     # st.dataframe(
#     #     highest_risk_cities,
#     #     use_container_width=True
#     # )


#     # # HIGH-RISK PERIODS

#     # st.header("High-Risk Forecast Periods")

#     # st.dataframe(
#     #     high_risk_periods,
#     #     use_container_width=True
#     # )


#     # # HEAVY RAIN

#     # st.header("Heavy Rain Conditions")

#     # st.dataframe(
#     #     heavy_rain,
#     #     use_container_width=True
#     # )


#     # # STRONG WIND

#     # st.header("Strong Wind Conditions")

#     # st.dataframe(
#     #     strong_wind,
#     #     use_container_width=True
#     # )


#     # # EXTREME TEMPERATURE

#     # st.header("Extreme Temperature Conditions")

#     # st.dataframe(
#     #     extreme_temperature,
#     #     use_container_width=True
#     # )


#     # # TOP RISK DAYS

#     # st.header("Top Risk Days")

#     # st.dataframe(
#     #     top_risk_days,
#     #     use_container_width=True
#     # )


#     df = pd.DataFrame(get_map_data() , columns=["city","latitude","longitude" , "date" , "risk" , "risk_level"])

#     color_map = {
#         "low": "#2ecc71",             
#         "medium": "#f1c40f",          
#         "high": "#e67e22",            
#         "very high": "#e74c3c",       
#         "extremely high": "#8e44ad",  
#     }

#     df["color"] = df["risk_level"].map(color_map)

#     st.map(
#         df,
#         latitude="latitude",
#         longitude="longitude",
#         size="risk",           
#         color="color"  
#     )



import streamlit as st
import pandas as pd
import plotly.express as px

from transformation.gold import gold_data
from queries.queries import get_map_data


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Morocco Weather Risk Dashboard",
    page_icon="🌦️",
    layout="wide"
)


# ============================================================
# DATA
# ============================================================

df = pd.DataFrame(
    get_map_data(),
    columns=[
        "city",
        "latitude",
        "longitude",
        "date",
        "risk",
        "risk_level"
    ]
)

df["date"] = pd.to_datetime(df["date"])

gold = gold_data.copy()
gold["date"] = pd.to_datetime(gold["date"])


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🔎 Filters")

st.sidebar.markdown("Filter the dashboard by:")


# City filter
cities = sorted(df["city"].unique())

selected_cities = st.sidebar.multiselect(
    "City",
    options=cities,
    default=cities
)


# Risk level filter
risk_levels = [
    "low",
    "medium",
    "high",
    "very high",
    "extremely high"
]

selected_risk_levels = st.sidebar.multiselect(
    "Risk level",
    options=risk_levels,
    default=risk_levels
)


# Date filter
min_date = df["date"].min().date()
max_date = df["date"].max().date()

selected_dates = st.sidebar.date_input(
    "Date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)


# Period filter
period = st.sidebar.selectbox(
    "Period",
    [
        "All",
        "Morning",
        "Afternoon",
        "Evening"
    ]
)


# ============================================================
# FILTER DATA
# ============================================================

filtered_df = df[
    (df["city"].isin(selected_cities)) &
    (df["risk_level"].isin(selected_risk_levels))
].copy()


if len(selected_dates) == 2:

    start_date = pd.Timestamp(selected_dates[0])
    end_date = pd.Timestamp(selected_dates[1])

    filtered_df = filtered_df[
        (filtered_df["date"] >= start_date) &
        (filtered_df["date"] <= end_date)
    ]


# Match the selected cities/dates with Gold data
filtered_gold = gold[
    (gold["city"].isin(selected_cities))
].copy()


if len(selected_dates) == 2:

    filtered_gold = filtered_gold[
        (filtered_gold["date"] >= start_date) &
        (filtered_gold["date"] <= end_date)
    ]


# ============================================================
# HEADER
# ============================================================

st.title("🌦️ Morocco Weather Risk Dashboard")

st.markdown(
    """
    ### Weather conditions and operational risk

    This dashboard monitors weather forecasts across Moroccan cities
    and identifies periods that may create operational risks for
    delivery and logistics activities.

    Use the filters on the left to explore specific cities, dates,
    periods, and risk levels.
    """
)


# ============================================================
# KPIs
# ============================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🏙️ Cities",
        filtered_df["city"].nunique()
    )

with col2:
    if len(filtered_gold) > 0:
        st.metric(
            "🌡️ Max Temperature",
            f"{filtered_gold['temp_max'].max():.1f} °C"
        )
    else:
        st.metric("🌡️ Max Temperature", "—")

with col3:
    if len(filtered_gold) > 0:
        st.metric(
            "🌧️ Max Precipitation",
            f"{filtered_gold['precipitation'].max():.1f} mm"
        )
    else:
        st.metric("🌧️ Max Precipitation", "—")

with col4:
    high_risk_count = filtered_df[
        filtered_df["risk_level"].isin(
            ["high", "very high", "extremely high"]
        )
    ].shape[0]

    st.metric(
        "⚠️ High-Risk Periods",
        high_risk_count
    )


st.divider()


# ============================================================
# MAP
# ============================================================

st.subheader("🗺️ Weather Risk Map")

st.markdown(
    "Each point represents a city. Larger points indicate higher risk."
)


map_colors = {
    "low": "#2ecc71",             # green
    "medium": "#f1c40f",          # yellow
    "high": "#e67e22",            # orange
    "very high": "#e74c3c",       # red
    "extremely high": "#8e44ad"   # purple
}

filtered_df["color"] = filtered_df["risk_level"].map(map_colors)


if len(filtered_df) > 0:

    st.map(
        filtered_df,
        latitude="latitude",
        longitude="longitude",
        size="risk",
        color="color"
    )

else:

    st.warning("No cities match the selected filters.")


# ============================================================
# MAP LEGEND
# ============================================================

st.markdown("#### Risk level")

legend_col1, legend_col2, legend_col3, legend_col4, legend_col5 = st.columns(5)

with legend_col1:
    st.markdown("🟢 **Low**")

with legend_col2:
    st.markdown("🟡 **Medium**")

with legend_col3:
    st.markdown("🟠 **High**")

with legend_col4:
    st.markdown("🔴 **Very High**")

with legend_col5:
    st.markdown("🟣 **Extremely High**")


st.divider()


# ============================================================
# WEATHER DISTRIBUTIONS
# ============================================================

st.subheader("📊 Weather Conditions")


if len(filtered_gold) > 0:

    col1, col2, col3 = st.columns(3)


    # --------------------------------------------------------
    # TEMPERATURE
    # --------------------------------------------------------

    with col1:

        temp_data = (
            filtered_gold["temp_max_category"]
            .value_counts(normalize=True)
            .mul(100)
            .reset_index()
        )

        temp_data.columns = ["Temperature", "Percentage"]

        fig_temp = px.bar(
            temp_data,
            x="Temperature",
            y="Percentage",
            title="🌡️ Temperature Distribution",
            text_auto=".1f"
        )

        fig_temp.update_layout(
            yaxis_title="Percentage (%)",
            xaxis_title=""
        )

        st.plotly_chart(
            fig_temp,
            use_container_width=True
        )


    # --------------------------------------------------------
    # RAIN
    # --------------------------------------------------------

    with col2:

        rain_data = (
            filtered_gold["rain_category"]
            .value_counts(normalize=True)
            .mul(100)
            .reset_index()
        )

        rain_data.columns = ["Rain", "Percentage"]

        fig_rain = px.bar(
            rain_data,
            x="Rain",
            y="Percentage",
            title="🌧️ Rain Distribution",
            text_auto=".1f"
        )

        fig_rain.update_layout(
            yaxis_title="Percentage (%)",
            xaxis_title=""
        )

        st.plotly_chart(
            fig_rain,
            use_container_width=True
        )


    # --------------------------------------------------------
    # WIND
    # --------------------------------------------------------

    with col3:

        wind_data = (
            filtered_gold["wind_category"]
            .value_counts(normalize=True)
            .mul(100)
            .reset_index()
        )

        wind_data.columns = ["Wind", "Percentage"]

        fig_wind = px.bar(
            wind_data,
            x="Wind",
            y="Percentage",
            title="💨 Wind Distribution",
            text_auto=".1f"
        )

        fig_wind.update_layout(
            yaxis_title="Percentage (%)",
            xaxis_title=""
        )

        st.plotly_chart(
            fig_wind,
            use_container_width=True
        )


else:

    st.info("No weather data matches the selected filters.")


# ============================================================
# RISK OVER TIME
# ============================================================

st.divider()

st.subheader("📈 Risk Over Time")


if len(filtered_df) > 0:

    risk_over_time = (
        filtered_df
        .groupby("date", as_index=False)["risk"]
        .mean()
    )

    fig_risk = px.line(
        risk_over_time,
        x="date",
        y="risk",
        markers=True,
        title="Average Weather Risk"
    )

    fig_risk.update_layout(
        xaxis_title="Date",
        yaxis_title="Risk Score",
        yaxis_range=[0, 100]
    )

    st.plotly_chart(
        fig_risk,
        use_container_width=True
    )


# ============================================================
# HIGH RISK CITIES
# ============================================================

st.divider()

st.subheader("⚠️ Highest-Risk Cities")

if len(filtered_df) > 0:

    high_risk_cities = (
        filtered_df
        .groupby("city", as_index=False)["risk"]
        .max()
        .sort_values("risk", ascending=False)
        .head(10)
    )

    fig_cities = px.bar(
        high_risk_cities,
        x="risk",
        y="city",
        orientation="h",
        title="Maximum Risk by City",
        text_auto=".1f"
    )

    fig_cities.update_layout(
        xaxis_title="Risk Score",
        yaxis_title="",
        xaxis_range=[0, 100]
    )

    st.plotly_chart(
        fig_cities,
        use_container_width=True
    )