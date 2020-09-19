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


# In[11]:


sql = "select name from sqlite_master" "where type = 'table';"


# In[12]:


sales_data_df.head()  


# In[20]:


# second attempt 
import pandas as pd
from sqlalchemy import create_engine
#connect to sqlite db
db_file = r'Users/mlmfe/Downloads/salesdata.db'
#create engine
engine = create_engine(r"sqlite:///{}".format(db_file))
sql ="select name from sqlite_master where type = 'table'"
sales_tablename_df = pd.read_sql(sql, engine)
sales_tablename_df


# In[10]:


get_ipython().run_line_magic('pinfo', 'sales_data_df.read_sql')


# In[ ]:




