import pandas as pd


#MERGING APIS

def merging_all():

    #MERGE API
    merge_api = pd.merge(rename_database, rename_api, how='inner', on='job')
    data_plus_api = merge_api[["uuid", "country_code", "suggestion", "gender"]]

    # MERGE CON EL SCRAPPING (deberia salir scrapping_df)
    merge_scrapping = pd.merge(data_plus_api, acrapping_df, how='inner', on='country_code')

    return merge_scrapping[["country", "suggestion", "gender"]]


#Drop las merge (esto deberia ir antes)
dropped_table.loc[~(dropped_table==0).all(axis=1)]



#Cleaning

data_plus_scrapping["gender"].replace(to_replace = ['male', 'Fem', 'FeMale','female'], value = ['Male', 'Female', 'Female','Female'],inplace=True)

#new column
count_column = data_plus_scrapping.groupby(['country', 'suggestion', 'gender']).agg({'suggestion': 'count'})
count_column.columns = ['cantidad']
test = count_column.reset_index()
total_count = test['cantidad'].sum()

#new column (2)
test['Percentage'] = (test['cantidad'] / test['cantidad'].sum()*100).round(2).astype(str) + '%'