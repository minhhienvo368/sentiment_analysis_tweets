# Import Module
import os
import twint
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

import nest_asyncio
nest_asyncio.apply()

# Set up TWINT config
c = twint.Config()
c.Search = "#SquidGame"

# Custom output format
c.Lang = "en"
c.Limit = 40000
c.Store_csv = True
c.Output = "squidgame_data.csv"
twint.run.Search(c)

#Read data from csv file
df_squidgame = pd.read_csv("../data/raw/squidgame_data.csv") 
df_maid = pd.read_csv("../data/raw/Maid_data.csv") 
df_netflix = pd.read_csv("../data/raw/Netflix_data.csv") 
df_theguilty = pd.read_csv("../data/raw/TheGuilty_data.csv") 
df_midnightmass = pd.read_csv("../data/raw/MidnightMass.csv") 

#Filter data 
df_squidgame_en = pd.DataFrame(df_squidgame[df_squidgame.language == 'en'])
df_maid_en = pd.DataFrame(df_maid[df_maid.language == 'en'])
df_netflix_en = pd.DataFrame(df_netflix[df_netflix.language == 'en'])
df_theguilty_en = pd.DataFrame(df_theguilty[df_theguilty.language == 'en'])
df_midnightmass_en = pd.DataFrame(df_midnightmass[df_midnightmass.language == 'en'])

#Take some columns for data analysis purposes
df_squidgame_en = df_squidgame_en[['tweet', 'username','likes_count', 'date']].copy()
df_maid_en = df_maid_en[['tweet', 'username','likes_count', 'date']].copy()
df_netflix_en = df_netflix_en[['tweet', 'username','likes_count', 'date']].copy()
df_theguilty_en = df_theguilty_en[['tweet', 'username','likes_count', 'date']].copy()
df_midnightmass_en = df_midnightmass_en[['tweet', 'username','likes_count', 'date']].copy()

#Save data to csv files
df_squidgame_en = df_squidgame_en.reset_index(drop=True).to_csv('../data/df_squidgame_en.csv',index=False)
df_maid_en = df_maid_en.reset_index(drop=True).to_csv('../data/df_maid_en.csv',index=False)
df_netflix_en = df_netflix_en.reset_index(drop=True).to_csv('../data/df_netflix_en.csv',index=False)
df_theguilty_en = df_theguilty_en.reset_index(drop=True).to_csv('../data/df_theguilty_en.csv',index=False)
df_midnightmass_en = df_midnightmass_en.reset_index(drop=True).to_csv('../data/df_midnightmass_en.csv',index=False)

