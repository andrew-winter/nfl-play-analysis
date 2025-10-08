import json
import os
import pandas as pd
import re
import requests
#import sqlite3
from bs4 import BeautifulSoup
from scripts.download_nflverse_csv import download_nflverse_csv
from scripts.read_nflverse_dictionary import read_nflverse_dictionary

nflverse_url = "https://github.com/nflverse/nflverse-data/releases/download"
#connection = sqlite3.connect("data\dbs\pbp.sqlite")

# %%
# Dictionary comprehension to map dtypes to field names
data_dictionary = read_nflverse_dictionary()
pbp_dtypes = {dy["field"]: dy["pdtype"] for dy in data_dictionary.to_dict("records")}
#data_dictionary.to_sql(name="data_dictionary", con=connection, if_exists="fail")

# %%
# Download pbp data
pbp_directory = os.path.join(os.getcwd(), "data", "pbp")
year_min = 2010
year_max = 2024
for yr in range(year_min, year_max + 1):
    download_nflverse_csv(f"{nflverse_url}/pbp/play_by_play_{yr}.csv", directory=pbp_directory, label="pbp")
    pbp = pd.read_csv(os.path.join(pbp_directory, f"play_by_play_{yr}.csv"), dtype=pbp_dtypes)
    pbp["last_updated"] = pd.Timestamp.now()
    #pbp.to_sql(name=f"pbp_{yr}", con=connection, if_exists="fail")
