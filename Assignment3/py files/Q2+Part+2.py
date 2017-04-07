
# coding: utf-8

# #  # Question2_Part2
# 
#  • Data contains fiscal and calendar year information. Same employee details exist twice in the dataset. Filter data by calendar year and find average salary (you might have to find average for each of the columns for every employee. Eg. Average of Total Benefits, Average of total compensation etc.) for every employee. - Now, find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
#  • For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column to hold the percentage value. 
#  • Displaythe top 5 Job Families according to this percentage value usingdf.head().
#  • Write the output (jobs and percentage value) to a csv.

# In[5]:

import os
path=os.getcwd()


# In[6]:

final_path=path+ "\\Data\\employee_compensation.csv"


# In[7]:

import pandas as pd
from pandas import DataFrame
import datetime


# In[8]:

#fields=['Year','Employee Identifier','Job Family', 'Total Benefits', 'Total Compensation', 'Salaries', 'Overtime']
df1=pd.read_csv(final_path, skipinitialspace=True)
df1 = df1.loc[df1['Year Type'] == 'Calendar'] # Filter out fiscal year data
#print(df1.head())


# In[9]:

df1=pd.DataFrame(df1.groupby(['Employee Identifier','Job Family']).mean())


# In[10]:

df1.drop(['Year', 'Organization Group Code','Union Code'], axis=1, inplace=True)
#df1.head()


# In[11]:

#Calculating people whose overtime salary is greater than 5% total salary
df2=df1[(df1['Overtime']>(.05*df1['Salaries']))]


# In[12]:

df2=df2.groupby([df2.index.get_level_values(1)]).mean()


# In[14]:

#Calculatung Percent_Total_Benefit
df2=df2[['Total Benefits','Total Compensation']]
df2['Percent_Total_Benefit']=100*(df2['Total Benefits']/df2['Total Compensation'])
df2=df2.sort_values(['Percent_Total_Benefit'], ascending=[False])
#df2.head(5)


# In[15]:

df2.to_csv('Q2_Part_2_Output.csv', sep=',')


# In[ ]:



