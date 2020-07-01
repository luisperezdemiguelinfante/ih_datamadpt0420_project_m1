import pandas as pd
from sqlalchemy import create_engine

#sqlitedb_path = '/Users/luisdemiguel/Desktop/Ironhack/ih_datamadpt0420_project_m1/data/raw/raw_data_project_m1.db'

def acquire(sqlitedb_path):
    #Bringing the database
    engine = create_engine(f'sqlite:///{sqlitedb_path}')

    #table country info
    country_info = pd.read_sql_query("select * from country_info", engine)
    country_info.replace(to_replace=["GB","GR"],value=["UK","EL"],inplace=True)

    #table career info
    career_info = pd.read_sql_query("select * from career_info", engine)

    #table personal info
    personal_info = pd.read_sql_query("select * from personal_info", engine)


    #Merging all 3 tables
    between_info = pd.merge(country_info, career_info,how='inner', on='uuid')
    merge_info = pd.merge(between_info, personal_info,how='inner', on='uuid')
    filtered_info = merge_info[["uuid", "country_code", "normalized_job_code", "gender"]]

    #rename
    rename_database = filtered_info.rename(columns={"normalized_job_code": "job"})
    return rename_database