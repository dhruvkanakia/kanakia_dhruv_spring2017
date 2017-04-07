
# coding: utf-8

# # # Q1_PART TWO
# 
#    Use ‘vehicle_collisions’ data set.
#    For each borough, find out distribution of each collision scale. (One car involved? Two? Three? or more?) (From 2015   to present)
#    Display a few rows of the outputuse df.head().
#    Generate a csv output with five columns ('borough', 'one-vehicle', 'two-vehicles', 'three-vehicles', 'more-vehicles')

# In[1]:

import os
a=os.getcwd()


# In[2]:

path= a+"\\Data\\vehicle_collisions.csv"


# In[3]:

import pandas as pd
from pandas import DataFrame
import numpy as np
import datetime
from pandas import Series, DataFrame
fields=['BOROUGH', 'VEHICLE 1 TYPE', 'VEHICLE 2 TYPE','VEHICLE 2 TYPE', 'VEHICLE 3 TYPE', 'VEHICLE 4 TYPE', 'VEHICLE 5 TYPE' ]
df=pd.read_csv(path, skipinitialspace=True, usecols=fields)
#print(df1.head())


# In[4]:

df['VEHICLE 1 TYPE'] = df['VEHICLE 1 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)
df['VEHICLE 2 TYPE'] = df['VEHICLE 2 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)
df['VEHICLE 3 TYPE'] = df['VEHICLE 3 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)
df['VEHICLE 4 TYPE'] = df['VEHICLE 4 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)
df['VEHICLE 5 TYPE'] = df['VEHICLE 5 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)
df['TOTAL'] = df['VEHICLE 1 TYPE']+df['VEHICLE 2 TYPE']+df['VEHICLE 3 TYPE']+df['VEHICLE 4 TYPE']+df['VEHICLE 5 TYPE']


# In[5]:

df['1 VEHICLE INVOLVED']= np.where(df['TOTAL'] == 1, 1,0)
df['2 VEHICLE INVOLVED']= np.where(df['TOTAL'] == 2, 1,0)
df['3 VEHICLE INVOLVED']= np.where(df['TOTAL'] == 3, 1,0)
df['MORE VEHICLES INVOLVED']= np.where(df['TOTAL'] >= 4, 1,0)
df=df.groupby('BOROUGH').sum()


# In[6]:

df=DataFrame(df,columns=['1 VEHICLE INVOLVED','2 VEHICLE INVOLVED','3 VEHICLE INVOLVED','MORE VEHICLES INVOLVED'])


# In[7]:

df.to_csv('Q1_Part2.csv', sep=',')


# In[ ]:



