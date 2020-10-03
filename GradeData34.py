#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("C:/Users/mlmfe/OneDrive/Desktop/BI/gradedata.csv")
df.head()


# In[7]:


# Create the bin dividers 
bins = [0, 60, 70, 80, 90, 100]
# Create names for the four groups 
group_names = ['F', 'D', 'C', 'B', 'A']
df['lettergrade'] = pd.cut(df['grade'], bins, labels=group_names) 
df


# In[14]:


bins = [0, 60, 70, 80, 90, 100] 
# Create names for the four groups 
group_names = ['Fail','Fail', 'Fail','Pass', 'Pass']
df['passorfail'] = pd.cut(df['grade'], bins, labels=group_names) 
df


# In[6]:


pd.value_counts(df['lettergrade'])


# In[ ]:




