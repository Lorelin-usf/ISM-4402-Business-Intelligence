#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("C:/Users/mlmfe/OneDrive/Desktop/BI/gradedata.csv")
df.head()


# In[5]:


import numpy as np 
df['isFailing'] = np.where(df['grade']<70, 'yes', 'no')
df.tail(10)


# In[6]:


df['isFailingMale'] = np.where((df['grade']<70) & (df['gender'] == 'male'),'yes', 'no') 
df.tail(10)


# In[16]:


#Your turn 
import numpy as np
df['timemgmt'] = np.where((df['exercise'] > 3) & (df['hours'] > 17),'busy')
df.tail(5)


# In[ ]:




