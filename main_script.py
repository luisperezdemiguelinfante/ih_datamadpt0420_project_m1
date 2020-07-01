import argparse
from modules import database
from modules import apis
from modules import web_scrapping
from modules import gathering_cleaning


def argument_parser():
    parser = argparse.ArgumentParser(description= 'select a country...')
    parser.add_argument("-c", "--country", type = str, dest = 'country', required = False, help = 'country definition...')
    arg = parser.parse_args()
    return arg

def main(country):
    print("starting_pipeline")
    sqlitedb_path = 'data/raw/raw_data_project_m1.db'
    db_df = database.acquire(sqlitedb_path)
    print('printing db_df', db_df.head())
    url = 'http://api.dataatwork.org/v1/jobs/autocomplete?contains=data'
    apis_df = apis.enrich_country_codes(url)
    print('apis response', apis_df.head())
    scrapping_url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
    scrapping_df = web_scrapping.including_scrapping(scrapping_url)
    print('with_scrapping', scrapping_df.head())
    merged_dataframe = gathering_cleaning.merging_all(db_df, apis_df, scrapping_df, country)
    print(merged_dataframe)

    merged_dataframe.to_csv(r'data/results/luis_perez.csv', index=False)



if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments.country)

