from google.cloud import bigquery
import pandas as pd
import streamlit as st


def fetch_sandi_data(table_name: str="sensei-seeker.sandi.profiles_2024") -> pd.DataFrame:
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
    query = f"""
        SELECT *
        FROM bigquery-public-data.ml_datasets.iris
    """
    
    return client.query(query).to_dataframe()


def fetch_census_data() -> pd.DataFrame:
    client = bigquery.Client(project="sensei-seeker", location="US")
    query = f"""
        SELECT *
        FROM bigquery-public-data.ml_datasets.census_adult_income
    """
    return client.query(query).to_dataframe()
   