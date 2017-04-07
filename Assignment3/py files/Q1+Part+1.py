
# coding: utf-8

# # # Q1_PART ONE
#  • Use "vehicle_collisions"  data set.
#  • For each month in 2016, find out the percentage of collisions in Manhattan out of that year's total accidents in New  York City. 
#  • Display a few rows of the output use df.head ().
#  • Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’, ‘Percentage’)

# In[2]:

import os
path=os.getcwd()


# In[ ]:




# In[4]:

final_path=path+ "\\Data\\vehicle_collisions.csv"


# In[8]:

#Reading csv file
import pandas as pd
from pandas import DataFrame
import datetime
fields=['DATE','BOROUGH']
df=pd.read_csv(final_path, skipinitialspace=True, usecols=fields)
#print(df.head())


# In[10]:

df['DATE']= pd.to_datetime(df.DATE)


# In[11]:

#df.head()


# In[12]:

df['Month']=df.DATE.dt.month


# In[13]:

df['Year']= df.DATE.dt.year


# In[14]:

#df.head()


# In[15]:

#df.loc[df['Year']==2016].head()


# In[16]:

df1=pd.DataFrame(df)


# In[17]:

#df1.head()


# In[18]:

df1=df1[(df1.Year == 2016)]


# In[19]:

df2 = df1.loc[:,['Month','Year']]   


# In[20]:

#df2.head()


# In[21]:

df3=df2.groupby('Month', sort=False).count().reset_index()  
#df3.head()


# In[22]:

df_Manhattan= df1[(df1.BOROUGH == "MANHATTAN")]


# In[23]:

df_Manhattan_Month= df_Manhattan.groupby('Month', sort=False).count().reset_index()  
df_Manhattan_Month.head()
df_Manhattan_Month = df_Manhattan_Month.rename(columns={'BOROUGH':'MANHATTAN'})
#df_Manhattan_Month.head()


# In[24]:

del df_Manhattan_Month['Year']


# In[25]:

#df_Manhattan_Month.head()


# In[26]:

df_monthly= df_Manhattan_Month.merge(df3)


# In[27]:

#df_monthly.head()


# In[28]:

df_monthly['Percentage']= df_monthly['MANHATTAN']/df_monthly['Year']


# In[29]:

df_monthly['Percentage']=df_monthly['Percentage']*100


# In[30]:

#df_monthly.head()


# In[31]:

import calendar
df_monthly['Month'] = df_monthly['Month'].apply(lambda x: calendar.month_abbr[x])


# In[32]:

#df_monthly.head()


# In[33]:

df_monthly = df_monthly.rename(columns={'Year':'NYC'})


# In[34]:

df_monthly.head()


# In[35]:

df_monthly.to_csv('Q1_Part1.csv', sep=',')


# In[ ]:




# In[ ]:



