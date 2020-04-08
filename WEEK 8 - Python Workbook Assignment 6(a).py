#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "~/Downloads/learn-data-analysis-w-python-master/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[5]:


df = df.sort_values(['fname','lname','age','grade'])
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




