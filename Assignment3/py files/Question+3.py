
# coding: utf-8

# In[ ]:




# In[7]:

import pandas as pd
import numpy as np


# In[8]:

import os
path=os.getcwd()


# In[9]:

final_path=path+ "\\Data\\cricket_matches.csv"


# In[10]:

df= pd.read_csv(final_path)


# In[12]:

df['team'] = np.where((df['home'] == df['winner']), df['home'], np.nan)


# In[13]:

df1=df[df.home==df.winner]


# In[14]:

df1['winner_score'] = df[['innings1_runs','innings2_runs']].max(axis=1)


# In[17]:

df1=df1.groupby('home')['winner_score'].mean()


# In[18]:

df2 = df1.to_frame().reset_index()
df2['winner_score']= round(df2['winner_score'],2)


# In[19]:

df2.head()


# In[49]:

df2.to_csv('Q3.csv', sep=',')


# In[ ]:



