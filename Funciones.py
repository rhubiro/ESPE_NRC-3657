#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')

get_ipython().run_line_magic('matplotlib', 'notebook')


# In[6]:


x=np.linspace(-7,7,100)


# In[7]:


def f(x):
    return x**2-x+1
def g(x):
    return 2/(x-1)


# In[8]:


fig, ax=plt.subplots()
ax.plot(x,f(x))
ax.plot(x,g(x))

