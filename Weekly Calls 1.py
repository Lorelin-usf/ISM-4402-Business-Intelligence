#!/usr/bin/env python
# coding: utf-8

# In[21]:


import os
os.chdir ('C:Users/mlmfe/OneDrive/Desktop/BI/datasets_export/weekly_call_data')


# In[24]:


import pandas as pd 
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob("weekdata*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.head()


# In[ ]:





# In[ ]:




