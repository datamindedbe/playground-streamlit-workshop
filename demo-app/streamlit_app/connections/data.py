from google.cloud import bigquery
import pandas as pd


def fetch_covid_data() -> pd.DataFrame:
    """
    Fetches person profiles from BigQuery.

    Returns:
        pd.DataFrame: DataFrame containing covid data
    """
    client = bigquery.Client(project="sensei-seeker", location="US")
    query = """
        SELECT * FROM `bigquery-public-data.covid19_open_data.covid19_open_data` LIMIT 10
    """

    return client.query(query).to_dataframe()


def fetch_sandi_data(
    table_name: str = "sensei-seeker.sandi.profiles_2024",
) -> pd.DataFrame:
    """
    Fetches person profiles from BigQuery.

    Returns:
        pd.DataFrame: DataFrame containing profile data
    """
    client = bigquery.Client(project="sensei-seeker", location="EU")
    query = f"""
        SELECT Person, Level, Level_code, Level_number, Client 
        FROM {table_name}
    """

    return client.query(query).to_dataframe()


def fetch_iris_data() -> pd.DataFrame:
    client = bigquery.Client(project="sensei-seeker", location="US")
    query = """
        SELECT *
        FROM bigquery-public-data.ml_datasets.iris
    """

    return client.query(query).to_dataframe()


def fetch_census_data() -> pd.DataFrame:
    client = bigquery.Client(project="sensei-seeker", location="US")
    query = """
        SELECT *
        FROM bigquery-public-data.ml_datasets.census_adult_income
    """
    return client.query(query).to_dataframe()
