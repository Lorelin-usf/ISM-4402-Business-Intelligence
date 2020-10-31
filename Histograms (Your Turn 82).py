#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd 
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv("C:/Users/mlmfe/OneDrive/Desktop/BI/gradedata.csv")
df.head()
df.hist()


# In[3]:


df.hist(column="hours", by="gender")


# In[4]:


#Your turn 82 
df.hist(column="age", by="gender")


# In[ ]:




