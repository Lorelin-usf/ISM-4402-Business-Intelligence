#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/mlmfe/OneDrive/Desktop/BI/gradedata.csv")
df.head()


# In[2]:


import statsmodels.formula.api as sm
result = sm.ols( formula='grade ~ age + exercise + hours',
                data=df).fit()
result.summary()


# In[3]:


#your turn page 63
import statsmodels.formula.api as sm
result = sm.ols( formula='grade ~ gender + exercise + hours',
                data=df).fit()
result.summary()


# In[ ]:




