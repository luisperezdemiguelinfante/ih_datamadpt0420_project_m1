import pandas as pd


#MERGING APIS

def merging_all(db_df, api_df, scrapping_df, country):

    #MERGE API
    merge_api = pd.merge(db_df, api_df, how='inner', on='job')
    data_plus_api = merge_api[["uuid", "country_code", "suggestion", "gender"]]

    # MERGE CON EL SCRAPPING (deberia salir scrapping_df)
    merge_scrapping = pd.merge(data_plus_api, scrapping_df, how='inner', on='country_code')
    merge_scrapping = merge_scrapping[["country", "suggestion", "gender"]]
    merge_scrapping["gender"].replace(to_replace = ['male', 'Fem', 'FeMale','female'], value = ['Male', 'Female', 'Female','Female'],inplace=True)
    #if country != None:
        #merge_scrapping = merge_scrapping.filter()
    count_column = merge_scrapping.groupby(['country', 'suggestion', 'gender']).agg({'suggestion': 'count'})
    count_column.columns = ['cantidad']
    final_df = count_column.reset_index()

    final_df['Percentage'] = (final_df['cantidad'] / final_df['cantidad'].sum()*100).round(2).astype(str) + '%'

    return final_df
