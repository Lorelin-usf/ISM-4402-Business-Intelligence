#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/mlmfe/OneDrive/Desktop/BI/gradedata.csv")
df.head()


# In[12]:


df = df.sort_values(by=['grade', 'age'],ascending=[True, True]) 
df.head()


# In[14]:


#your turn page 60
df = df.sort_values(by=['fname','grade', 'age'],ascending=[True, True, True]) 
df.head(100)


# In[ ]:




