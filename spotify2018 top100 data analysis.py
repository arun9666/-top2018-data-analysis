#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


dataset=pd.read_csv('spotify2018.csv')


# In[3]:


dataset.head()


# In[4]:


dataset.head(10)


# In[5]:


dataset.shape


# In[6]:


dataset.columns


# In[7]:


dataset.index


# In[8]:


dataset.nunique()


# In[9]:


dataset['name'].dtype


# In[10]:


dataset['id'].dtype


# In[11]:


dataset['key'].dtype


# In[ ]:




