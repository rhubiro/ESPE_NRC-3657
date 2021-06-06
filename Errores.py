#!/usr/bin/env python
# coding: utf-8

# ## Cálculo del error relativo, error absoluto, error porcentual y las cifras significativas para los siguientes casos:
# 
# $$ x=0.005429, \bar{x}=0.00543 \\ x=189.3478, \bar{x}=18.93478 \\ x_0=4.367, x_1=4.3689$$

# ## valores

# In[24]:


x_1=0.005429
x_2=0.00543
x_3=189.3478
x_4=18.93478
x0=4.367
x1=4.3689


# ## Error relativo
# $$e_{rel}=\displaystyle\frac{\left|x-\bar{x}\right|}{\left|x\right|}$$

# In[25]:


e_rel_1=abs((x_1-x_2)/x_1)
e_rel_2=abs((x_3-x_4)/x_3)
print("El error relativo entre 0.005429 y 0.00543 es = ",e_rel_1)
print("El error relativo entre 189.3478 y 18.93478 es = ",e_rel_2)


# ## Error absoluto
# $$e_{abs}=\left|x-\bar{x}\right|$$

# In[26]:


e_abs_1=abs(x_1-x_2)
e_abs_2=abs(x_3-x_4)
print("El error absoluto entre 0.005429 y 0.00543 es = ",e_abs1)
print("El error absoluto entre 189.3478 y 18.93478 es = ",e_abs2)


# ## Error porcentual
# $$e_{porcentual}=e_{abs}*100$$

# In[32]:


e_porcentual_1=e_abs_1*100
e_porcentual_2=e_abs_2*100
print("El error porcentual entre 0.005429 y 0.00543 es = ",e_porcentual_1," %")
print("El error porcentual entre 189.3478 y 18.93478 es = ",e_porcentual_2," %")


# ## Error aproximado
# $$e_{aprox}={\displaystyle\frac{\left|x_i-x_{i-1}\right|}{\left|x_i\right|}}*100$$

# In[36]:


e_aprox=abs((x1-x0)/x1)*100
print("El error aproximado entre x0=4.367 y x1=4.3689 es",e_aprox)


# In[ ]:




