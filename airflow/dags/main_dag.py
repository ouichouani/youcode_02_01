from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

from extraction.bronze import get_all_cities_data
from load.load_data import insert_cities , insert_forecasts , add_city_id


with DAG(
    dag_id="main",
    start_date=datetime(2025, 9, 21),
    schedule=None,
    catchup=False,
) as dag:

    # extract data and save each city in a jsno file with it's data using api calls
    extract_data = PythonOperator(
        task_id="get_all_cities_data",
        python_callable=get_all_cities_data,
    )

    # trensform data and calculate the risk + insert cities in database
    insert_cities_in_db = PythonOperator(
        task_id="insert_cities",
        python_callable=insert_cities,
    )

    # insert forecasts data in database
    insert_forecasts_in_db = PythonOperator(
        task_id="add_city_id",
        python_callable=add_city_id,
    )

    # insert forecasts data in database
    insert_forecasts_in_db = PythonOperator(
        task_id="insert_forecasts",
        python_callable=insert_forecasts,
    )


    extract_data >> insert_cities_in_db >> insert_forecasts_in_db 