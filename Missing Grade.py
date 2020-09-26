#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
df = pd.read_csv("C:/Users/mlmfe/OneDrive/Desktop/BI/missinggrade.csv")
df.head()


# In[6]:


#drop rows with missing data
df_no_missing = df.dropna()
df_no_missing


# In[7]:


#Add a column with Empty Values
import numpy as np
df['newcol'] = np.nan
df.head()


# In[8]:


#drop completely empty columns
df.dropna(axis=1, how='all')


# In[9]:


#Replace empty cells with 0
df.fillna(0)


# In[11]:


# fill missing grades with the mean value of grade 
# replace empty cells with average of column
df["grade"].fillna(df["grade"].mean(), inplace=True)
#implace = True means that the changes are saved to the dataframe right away


# In[15]:


#Fill missing grades with each gender's mean value of grade
df["grade"].fillna(df.groupby("gender")["grade"].transform("mean"), inplace = True)
     
                   


# In[16]:


#Your turn


# In[17]:


import pandas as pd
df = pd.read_csv("C:/Users/mlmfe/OneDrive/Desktop/BI/missinggrade.csv")
df.head()


# In[20]:


df.loc[df['grade'] <= 100]


# In[22]:


df.loc[(df['grade'] <= 0, 'grade')] = 0


# In[25]:


import pandas as pd 
names = ['Bob','Jessica','Mary','John','Mel'] 
grades = [76,-2,77,78,101] 
GradeList = zip(names,grades) 
df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades']) 
df


# In[32]:


df.loc[(df['Grades'] >= 100,'Grades')] = 100


# In[30]:


#YOUR TURN
import pandas as pd 
names = ['Bob','Jessica','Mary','John','Mel'] 
grades = [76,-2,77,78,101] 
GradeList = zip(names,grades) 
df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades']) 
df.loc[(df['Grades'] <= 0, 'Grades')] = 0


# In[ ]:




