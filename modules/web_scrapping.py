import requests
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
import re

def including_scrapping(scrapping_url):

    page = requests.get(scrapping_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    list=soup.find_all('td')
    a=len(list)
    lista=[]
    for i in range (a):
        w=soup.find_all('td')[i].get_text()
        ws= re.sub("\n", "", w)
        wws=re.sub(" ","",ws)
        if len(ws)>=4:
            lista.append(wws)
        else:
            pass

    rows_parsed = [row for row in lista]
    row_split = 2
    rows_refactored = [rows_parsed[x:x+row_split] for x in range(0, len(rows_parsed), row_split)]

    scrapping_df = pd.DataFrame(rows_refactored, columns = ['country', 'country_code'])
    scrapping_df['country_code'] = scrapping_df['country_code'].str.replace('(', '')
    scrapping_df['country_code'] = scrapping_df['country_code'].str.replace(')', '')

    return scrapping_df
