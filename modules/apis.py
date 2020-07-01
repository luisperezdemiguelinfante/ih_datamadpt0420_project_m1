import requests
import pandas as pd


def enrich_country_codes(url):
    response = requests.get(url)
    json_data = response.json()

    #convert to dataframe
    data_api = pd.DataFrame(json_data)

    #rename api to match
    rename_api = data_api.rename(columns={"uuid": "job"})

    #merge both data

    #merge_api = pd.merge(rename_database, rename_api, how='inner', on='job')
    #data_plus_api = merge_api[["uuid", "country_code", "suggestion", "gender"]]

    return rename_api