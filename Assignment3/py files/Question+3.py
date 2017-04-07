
# coding: utf-8

# In[ ]:




# In[10]:

import pandas as pd
import numpy as np


# In[1]:

import os
path=os.getcwd()


# In[4]:

final_path=path+ "\\Data\\cricket_matches.csv"


# In[25]:

df= pd.read_csv(final_path)


# In[33]:




# In[43]:

df['winner_score'] = df[['innings1_runs','innings2_runs']].max(axis=1)


# In[46]:

df1=df.groupby('winner')['winner_score'].mean()


# In[47]:

df2 = df1.to_frame().reset_index()
df2['winner_score']= round(df2['winner_score'],2)


# In[48]:

df2.head()


# In[49]:

df2.to_csv('Q3.csv', sep=',')


# In[ ]:



