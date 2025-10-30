import os
from pathlib import Path
from google.cloud import bigquery
import pandas as pd
import streamlit as st


APP_DIR = "streamlit_app"
SQL_QUERIES_DIR = "sql_queries"


def load_query(filepath: str) -> str:
    """Loads a SQL query from a .sql file."""
    try:
        return Path(filepath).read_text()
    except FileNotFoundError:
        st.error(f"Error: SQL file not found at {filepath}")
        return ""


def fetch_belgian_weather_data(project_id: str = "sensei-seeker") -> pd.DataFrame:
    """The SQL logic is stored in 'get_belgian_weather.sql'."""

    # Load the query from the separate .sql file
    sql_query = load_query(
        os.path.join(os.getcwd(), APP_DIR, SQL_QUERIES_DIR, "get_belgian_weather.sql")
    )

    if not sql_query:
        st.stop()

    client = bigquery.Client(project=project_id, location="US")

    return client.query(sql_query).to_dataframe()
