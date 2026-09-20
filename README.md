# 🌦️ Morocco Weather Risk Pipeline

A complete data engineering project that collects weather forecasts for Moroccan cities, transforms and analyzes the data, calculates a weather risk score, and presents the results through an interactive Streamlit dashboard.

## 📌 Project Overview

This project aims to help a delivery and logistics company anticipate weather-related disruptions across Moroccan cities.

The pipeline combines city data from **SimpleMaps** with daily weather forecasts from **Open-Meteo** to identify cities and periods with the highest potential weather risks.

The project follows a **Bronze → Silver → Gold** data architecture and automates the complete workflow using **Apache Airflow**.

The final data is stored in **PostgreSQL** and visualized through a **Streamlit dashboard**.

## 🎯 Main Objectives

* Collect Moroccan city data and coordinates from SimpleMaps.
* Retrieve daily weather forecasts from Open-Meteo.
* Store and preserve raw data in the Bronze layer.
* Clean and validate data in the Silver layer.
* Create useful weather features in the Gold layer.
* Calculate a **Weather Risk Score from 0 to 100**.
* Store processed data in PostgreSQL.
* Avoid duplicates when updating forecasts.
* Perform SQL analysis to answer business questions.
* Create an interactive Streamlit dashboard.
* Automate the entire pipeline with Airflow.
* Handle API errors and task failures with retries.
* Containerize the environment using Docker Compose.

## 🎓 Context

This project was completed as part of a **data engineering project at YouCode**.

The goal was to work on a realistic business scenario where weather conditions can affect logistics and delivery operations.

The project allowed me to practice building an end-to-end data pipeline, from **data extraction and transformation to storage, analysis, visualization, and orchestration**.

## 🛠️ Technologies Used

* Python
* Pandas
* Open-Meteo API
* SimpleMaps
* PostgreSQL
* SQL
* Apache Airflow
* Streamlit
* Docker
* Docker Compose

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/ouichouani/youcode_02_01.git
```

### Start the project

Make sure **Docker** and **Docker Compose** are installed, then run:

```bash
docker compose up -d
```

The services will start inside their respective containers.

### Access the Dashboard

Open the Streamlit dashboard through the configured local URL.

### Access Airflow

Open the Airflow interface to monitor and manage the automated pipeline.

The pipeline can then be executed through Airflow to extract, transform, analyze, and load the latest weather data.
