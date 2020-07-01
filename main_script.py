import argparse
from notebooks import database
from notebooks import apis




def argument_parser():
    parser = argparse.ArgumentParser(description= 'select a country...')
    parser.add_argument("-c", "--country", type = str, dest = 'country', required = True, help = 'country definition...')
    arg = parser.parse_args()
    return arg

def main(country):
    print("starting_pipeline")
    sqlitedb_path = '/Users/luisdemiguel/Desktop/Ironhack/data-project-template/New Project/data/raw_data_project_m1.db'
    db_df = database.acquire(sqlitedb_path)
    print('printing db_df', db_df)
    url = 'http://api.dataatwork.org/v1/jobs/autocomplete?contains=data'
    apis_df= apis.enrich_country_codes(url)
    print('apis response', apis_df)
    scrapping_url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
    scrapping_df = web_crapping.including_scrapping(scrapping_url)
    print('with_scrapping', scrapping_df)
    merged_dataframe = Gathering_cleaning.merge_scrapping()
    print(merged_dataframe)



if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments.country)


# AQUI EMPIEZA EL CODIGO, HABRIA QUE CREAR UNA DEFINICION DE CADA UNA PARA QUE SE LAS VAYA TRAYENDO Y QUE HAGA EL MERGE?


#merge_api = pd.merge(rename_database, rename_api,how='inner', on='job')
#data_plus_api = merge_api[["uuid", "country_code", "suggestion", "gender"]]

#Drop las merge
#dropped_table.loc[~(dropped_table==0).all(axis=1)]



#MERGE CON EL SCRAPPING

#merge_scrapping = pd.merge(data_plus_api, df,how='inner', on='country_code')
#data_plus_scrapping = merge_scrapping [["country", "suggestion", "gender"]]
