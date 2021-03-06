#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/mlmfe/OneDrive/Desktop/BI/axisdata.csv")
df.head()


# In[4]:


# 1. Average Cars Sold Per Month

df['Cars Sold'].mean()


# In[5]:


# 2. Max cars sold per month
df['Cars Sold'].max()


# In[6]:


# 3. Min cars sold per month
df['Cars Sold'].min()


# In[14]:


# 4. Average cars sold per month by gender
df.groupby('Gender')['Cars Sold'].mean()


# In[26]:


# 5. Average hours worked by people selling more than three cars per month
df.groupby('Cars Sold')['Hours Worked'].mean()


# In[33]:


import pandas as pd
Sell = [34.159794,33.945545,33.184466,36.429487,43.440000]
AutoSale=zip(Sell)
df=pd.DataFrame(data=AutoSale, 
                columns=['Sell'])
df
df['Sell'].mean()


# In[7]:


# 6. Average years of experience
df['Years Experience'].mean()


# In[22]:


# 7. Average years of experience for people selling more than three cars per month
df.groupby('Cars Sold')['Years Experience'].mean()


# In[34]:


import pandas as pd
Experience = [ 3.175258,3.004950,2.961165,3.102564,3.800000]
ExpSale=zip(Experience)
df=pd.DataFrame(data=ExpSale,
               columns=['Experience'])
df
df['Experience'].mean()


# In[15]:


# 8. Average cars sold per month sorted by whether they have had sales training
df.groupby('SalesTraining')['Cars Sold'].mean()


# In[ ]:


# What do you think is the best indicator of a good salesperson?  
# A good indicator of being a good sales person is the average of 
# cars sold per month regardless of the years of experience. Although clearly there is a correlation between cars sold and years of experience showing that the more experience, the hihger the average of cars sold by a person.

