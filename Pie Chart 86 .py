#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
import pandas as pd 
get_ipython().run_line_magic('matplotlib', 'inline')
names = ['Bob','Jessica','Mary','John','Mel']
absences = [3,0,1,0,8]
detentions = [2,1,0,0,1]
warnings = [2,1,5,1,2]
GradeList = zip(names,absences,detentions,warnings)
columns=['Names','Absences','Detentions','Warnings']
df =pd.DataFrame(data= GradeList, columns=columns)
df['TotalDemerits']=df['Absences']+df['Detentions']+df['Warnings']
df


# In[7]:


df['TotalDemerits']=df['Absences']+df['Detentions']+df['Warnings']
df


# In[11]:


#YourTurn Page 84
plt.pie(df['TotalDemerits'],
       labels=df['Names'],
       explode=(0,0,0,0.15,0),
       startangle = 90,
       autopct='%1.1f%%',)
plt.axis('equal')
plt.show()


# In[12]:





# In[30]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
dataframe = pd.DataFrame
y = np.grade
x = np.hours
colors = np.random.rand(N)   
plt.scatter(dataframe.index, dataframe)


# In[ ]:




