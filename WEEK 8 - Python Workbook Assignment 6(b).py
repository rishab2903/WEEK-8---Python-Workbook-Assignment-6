#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "~/Downloads/learn-data-analysis-w-python-master/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ age + exercise + hours',data=df).fit()
result.summary()


# In[27]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ exercise + hours',data=df).fit()
result.summary()


# In[58]:


df.loc[df['gender']=='male','Total']=0


# In[62]:


df.loc[df['gender']=='female','Total']=1


# In[ ]:


df['gender']=df['total']


# In[68]:


df


# In[71]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ exercise + hours + gender',data=df).fit()
result.summary()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[39]:





# In[57]:





# In[ ]:





# In[ ]:





# In[65]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[55]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[47]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[42]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[36]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[69]:





# In[ ]:





# In[ ]:





# In[25]:





# In[26]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[21]:





# In[ ]:





# In[19]:





# In[30]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




