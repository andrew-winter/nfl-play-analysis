import json
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

# %%
def read_nflverse_dictionary():
    """Read nflverse play-by-play data dictionary.

    Use requests, bs4, and pandas to scrape the pbp data
    dictionary URL and convert to a Python dictionary.
    """
    url = 'https://nflreadr.nflverse.com/articles/dictionary_pbp.html'
    datatable_class = 'datatables html-widget html-fill-item'
    htmlwidget_id = 'htmlwidget-ac96cb3ee4656e2e9ec3'
    json_start = '"data":(\[.*\])'
    json_end = ',"container'
    
	r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
	# Locate the div with the specific class and id
    content = (
        soup
            .find('div', class_=datatable_class, id=htmlwidget_id)
            .find_next('script')
            .string)
    
    pattern = re.compile(rf'{json_start}{json_end}')
    match = pattern.search(content).group(1)
    json_loads = json.loads(match)
    
    df = pd.DataFrame({
        key: val for (key, val) in zip(['field', 'desc', 'type'], json_loads)})
    df.loc[df['type'] == 'numeric', 'pdtype'] = float
    df.loc[df['type'] == 'character', 'pdtype'] = str
    return df

# %%
#data_dictionary = read_nflverse_dictionary()