#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


import numpy as np


# In[ ]:


import glob


# In[ ]:


all_data = pd.DataFrame()


# In[9]:


for i in glob.glob("Desktop/datasets/weekly_call_data/weekdata_*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)


# In[ ]:


all_data.describe()


# In[ ]:





# In[ ]:




