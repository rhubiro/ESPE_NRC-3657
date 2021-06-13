#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0,2*np.pi)
r = .9 - 6*np.sin(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection="polar")
ax.plot(theta,r,"r") #"r", proporciona el color rojo para la curva

plt.show()


# In[ ]:




