#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/mlmfe/OneDrive/Desktop/BI/gradedata.csv")
df.head()


# In[7]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel'] 
grades = [76,83,77,78,95] 
GradeList = zip(names,grades) 
df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot()


# In[10]:


import matplotlib.pyplot as plt
df.plot()
displayText = "my annotation"
xloc = 1 
yloc = df['Grades'].max() 
xtext =8
ytext = 0
plt.annotate(displayText, 
             xy=(xloc, yloc), 
             xytext=(xtext,ytext), 
             xycoords=('axes fraction', 'data'), 
             textcoords='offset points')


# In[12]:


import matplotlib.pyplot as plt
df.plot()
displayText = "my annotation"
xloc = 1 
yloc = df['Grades'].max() 
xtext =8
ytext = -150
plt.annotate(displayText,
            xy=(xloc, yloc),
            arrowprops=dict(facecolor='black',shrink=0.05),
            xytext=(xtext,ytext),
            xycoords=('axes fraction', 'data'),
            textcoords='offset points')


# In[23]:


#Your turn page 74 
import matplotlib.pyplot as plt
df.plot()
displayText = "Wow!"
xloc = 1
yloc = 77 
xtext =-10
ytext = -200
plt.annotate(displayText,
            xy=(xloc, yloc),
            arrowprops=dict(facecolor='purple',shrink=1),
            xytext=(xtext,ytext),
            xycoords=('axes fraction', 'data'),
            textcoords='offset points')


# In[26]:


import matplotlib.pyplot as plt
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
status = ['Senior','Freshman','Sophomore','Senior','Junior']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
                 columns=['Names','grades'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='bar')


# In[30]:



import matplotlib.pyplot as plt
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
status = ['Senior','Freshman','Sophomore','Senior','Junior']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
                 columns=['status','names'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='bar')
df2 = df.set_index(df['status'])
df2.plot(kind="bar")


# In[31]:


#Your turn 76
import matplotlib.pyplot as plt
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
status = ['Senior','Freshman','Sophomore','Senior','Junior']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
                 columns=['status','names'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='bar')
df2 = df.set_index(df['status'])
df2.plot(kind="bar")


# In[ ]:




