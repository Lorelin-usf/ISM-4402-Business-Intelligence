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


# In[42]:


#Visualization 1
import pandas as pd
YearExp = [1,2,3,4,5,6,7]
AvgCarSold = [2.840909,2.825581,3.175258,3.004950,2.961165,3.102564,3.800000]
AutoSale=zip(YearExp,AvgCarSold)
df=pd.DataFrame(data= AutoSale,
               columns=['YearExp','AvgCarSold'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot()
displayText= "Average Cars Sold by  Years of Experience"
df2=df.set_index(df['YearExp'])


# In[45]:


import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/mlmfe/OneDrive/Desktop/BI/axisdata.csv")
df.head()
df['Gender'].count()


# In[47]:


df.groupby('Gender')['Gender'].count()


# In[48]:


df.groupby('Gender')['Cars Sold'].mean()


# In[53]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
Gender=['Male','Female']
TG=[510,489]
Genders=zip('Gender','TG')
columns=['Gender','TG']
df = pd.DataFrame(data=Genders, columns=columns)
df
plt.pie(df['Gender'])


# In[58]:


#Visualization 2
import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/mlmfe/OneDrive/Desktop/BI/axisdata.csv")
df.head()
df.hist(column="Hours Worked", by="Cars Sold")


# In[ ]:




