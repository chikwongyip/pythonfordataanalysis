# coding:utf-8
import pandas as pd
import numpy as np
import os

data_path = 'data/'

# 读取数据

df = (pd.read_csv(filepath_or_buffer=os.path.join(data_path, 'master.csv'))
      .rename(columns={'suicides/100k pop': 'suicides_per_100k',
                       ' gdp_for_year ($) ': 'gdp_year',
                       'gdp_per_capita ($)': 'gdp_capita',
                       'country-year': 'country_year'}).assign(
    gdp_year=lambda _df: _df['gdp_year'].str.replace(',', '').astype(np.int64))
      )

print(df.columns)

print(df['generation'].unique())

print(df.query('country == "Albania"'))