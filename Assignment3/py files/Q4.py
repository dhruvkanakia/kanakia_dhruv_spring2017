
# coding: utf-8

# # #  Question4
#   
# • Use ‘movies_awards’ data set.
#   • You are supposed to extract data from the awards column in this dataset and split it into several columns. An example is given below.
#   • The awards has details of wins, nominations in general and also wins and nominations in certain categories(e.g. Oscar, BAFTA etc.)
#   • You are supposed to create a win and nominated column (these 2 columns contain total number of wins and nominations) and other columns that extract the number of wins and nominations for each category of award. 
#   • If a movie has 2 Oscar nominations and 4 Oscar won, the columns Oscar_Awards_Won should have value 4 and Oscar_Awards_Nominated should have value 2. You should also have a total won and nominated column which aggregates all the awards (won or nominated). 
#   • Create two separate columns for each award category (won and nominated).
#   • Write your output to a csv file.

# In[39]:

import numpy as np
import pandas as pd
from pandas import DataFrame


# In[40]:

import os
path=os.getcwd()


# In[41]:

final_path=path+ "\\Data\\movies_awards.csv"


# In[42]:

#Reading csv file
df= pd.read_csv(final_path, skipinitialspace=True)


# In[43]:

df = df.fillna(0)


# In[44]:

df['Prime_Awards_Won']= df['Awards'].str.extract('Won (\d+) Primetime', expand=True).apply(pd.to_numeric)
df['Bafta_Awards_Won']= df['Awards'].str.extract('Won (\d+) BAFTA', expand=True).apply(pd.to_numeric)


# In[45]:

df['Prime_Awards_Nominated']= df['Awards'].str.extract('Nomination in (\d+) Primetime', expand=True).apply(pd.to_numeric)
df['Bafta_Awards_Nominated']= df['Awards'].str.extract('Nomination in (\d+) BAFTA', expand=True).apply(pd.to_numeric)


# In[46]:

df['Oscar_Awards_Won']= df['Awards'].str.extract('Won (\d+) Oscar', expand=True).apply(pd.to_numeric)
df['GoldenGlobeAwards_Won']= df['Awards'].str.extract('Won (\d+) Golden Globe', expand=True).apply(pd.to_numeric)


# In[47]:

df['Oscar_Awards_Nominated']= df['Awards'].str.extract('Nomination in (\d+) Oscar', expand=True).apply(pd.to_numeric)
df['GoldenGlobeAwards_Nominated']= df['Awards'].str.extract('Nomination in (\d+) Golden Globe', expand=True).apply(pd.to_numeric)


# In[48]:

df['Total_Awards_Won'] = df['Awards'].str.extract('(\d+) win', expand=True).apply(pd.to_numeric)
df['Total_Awards_Nominated'] = df['Awards'].str.extract('(\d+) Nominated', expand=True).apply(pd.to_numeric)


# In[49]:

#Replacing Nan with 0
df = df.fillna(0)


# In[50]:

# calculating total awards won
df['Total_Awards_Won'] = df['Total_Awards_Won']+df['Prime_Awards_Won']+df['Bafta_Awards_Won']+df['Oscar_Awards_Won']+df['GoldenGlobeAwards_Won']


# In[51]:

df['Total_Awards_Nominated']=df['Total_Awards_Nominated']+df['Prime_Awards_Nominated']+df['Bafta_Awards_Nominated']+df['Oscar_Awards_Nominated']+df['GoldenGlobeAwards_Nominated']


# In[52]:

df2=df[['Awards','Total_Awards_Won','Total_Awards_Nominated','Prime_Awards_Nominated','Oscar_Awards_Nominated','GoldenGlobeAwards_Nominated','Bafta_Awards_Nominated','Prime_Awards_Won','Oscar_Awards_Won','GoldenGlobeAwards_Won','Bafta_Awards_Won']]


# In[53]:

df2.head()


# In[54]:

df2 = df2[df2.Awards != 0] 


# In[55]:

df2.head()


# In[56]:

df2.to_csv('Q4.csv', sep=',')


# In[ ]:




# In[ ]:




# In[ ]:



