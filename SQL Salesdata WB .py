#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install ipython-sql')


# In[5]:


import pandas as pd
import numpy as np
import sqlite3 as sql


# In[8]:


#create connection to database file
database = "salesdata.db"
connection = sql.connect(database)


# In[13]:


query = '''SELECT * salesdata'''


# In[10]:


df= pd.read_sql_query(query, connection)
df.head()


# In[ ]:




