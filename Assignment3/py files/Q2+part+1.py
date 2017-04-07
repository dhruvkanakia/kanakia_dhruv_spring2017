
# coding: utf-8

# #  # Question2_Part1
# •Use 'employee_compensation' data set.
#  •Find out the highest paid departments in each organization group by calculating mean of total compensation for every  department.
#  •Output should contain the organization group and the departments in each organization group with the total compensationfrom highest to lowest value.
#  •Display a few rows of the outputuse df.head().
#  •Generate a csv output.
# 

# In[5]:

import os
path=os.getcwd()


# In[6]:

final_path=path+ "\\Data\\employee_compensation.csv"


# In[9]:

#Reading csv file
import pandas as pd
from pandas import DataFrame
import datetime
fields=['Organization Group','Department', 'Total Compensation']
df=pd.read_csv(final_path, skipinitialspace=True, usecols=fields)
#print(df.head())


# In[10]:

#Grouping by Organization Group and Department
df_borough= df.groupby(['Organization Group', 'Department']).mean()


# In[11]:

#Sorting in descending order
df_borough_sorted=df_borough.sort_values('Total Compensation', ascending=False)


# In[12]:

#df_borough_sorted.head()


# In[13]:

df_borough_sorted.to_csv('Q2_Part1.csv', sep=',')


# In[ ]:



