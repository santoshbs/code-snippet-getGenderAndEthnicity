#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 2022;
@author: santoshbs;
@purpose: Infer ethnicity based on the last name of a person; 
@package-used: https://pypi.org/project/ethnicolr/;
"""

import pandas as pd
from ethnicolr import census_ln

f= './persons.csv' #read the input data file 
df= pd.read_csv(f, low_memory= False)
df.columns

df_sub= df[df['person_country_code'] == 'US'] #filter as necessary
df_sub= df_sub[~df_sub['name_last'].isnull()]
df_sub['name_last'].head()

df_sub= df_sub['name_last']
df_sub= pd.DataFrame(df_sub)
df_sub= df_sub.drop_duplicates()

p= census_ln(df_sub, 'name_last') #obtain ethnicity information
p= p.rename(columns= {
    'pctwhite': 'ethnicity_inferred_percent_white',
    'pctblack': 'ethnicity_inferred_percent_black',
    'pctapi': 'ethnicity_inferred_percent_asianPacificIslander',
    'pctaian': 'ethnicity_inferred_percent_americanIndianAlaskanNative',
    'pct2prace': 'ethnicity_inferred_percent_twoOrMoreRaces',
    'pcthispanic': 'ethnicity_inferred_percent_hispanic',
    }) #rename columns for readability
p.columns
p= p.drop_duplicates(subset=['name_last'])
p.head()

df_ethnicity= df.merge(p, on= 'name_last', how= 'left') #merge with 

f= '/media/santoshbs/WD_BLACK/santosh/Gan-Organized/1-Projects-ONGOING/ELIE-YASIR/_data/_uspto_patentsview/_inferred/INVENTORS_inferred_ETHNICITY_usingPYEthnicolrAPI_v2.csv'
df_ethnicity.to_csv(f, index= False)

