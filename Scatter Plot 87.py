#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
dataframe = pd.DataFrame({'Col':
                         np.random.normal(size=200)})
plt.scatter(dataframe.index, dataframe['Col'])


# In[2]:


import numpy as np
import pandas as pd
df = pd.read_csv("C:/Users/mlmfe/OneDrive/Desktop/BI/gradedata.csv")
df.head()


# In[9]:


#your turn 87
import numpy as np
import pandas as pd
df = pd.read_csv("C:/Users/mlmfe/OneDrive/Desktop/BI/gradedata.csv")
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

y = np.grade
x = np.hours
colors = np.random.rand(N)   
plt.scatter(hours,grade)
plt.show()


# In[ ]:




