#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
c = pd.read_csv('http://bit.ly/Cars_file')
y = c.drop(c.iloc[:, 1:12:2], axis=1)
y.head()


# In[ ]:


c.loc[[0],["Model"]]


# In[ ]:


c.loc[[23], ['cyl']]


# In[ ]:


c.loc[[1,18,28], ['cyl','gear']]


# In[ ]:




