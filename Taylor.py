#!/usr/bin/env python
# coding: utf-8

# # Serie de Taylor
# $$\displaystyle\sum_{n=0}^\infty \frac{f^{(n)}(c)}{n!}(x-c)^n$$

# # Serie de Taylor para la función seno
# $$sen(x)=\displaystyle\sum_{n=0}^\infty \frac{(-1)^{(n)}}{(2n+1)!}x^{(2n+1)}$$

# # Declaración de variables

# In[1]:


import numpy as np
n=0
senx=0


# # Ingreso de ángulo

# In[2]:


print("Digite el valor del ángulo del que desea conocer el seno")
x=float(input())
#print("El ángulo ingresado es ",x)


# # Cálculo del seno del ángulo con 50 iteraciones

# In[3]:


y=60*np.math.pi/180
while(n!=50):
    signo=(-1)**n
    k=2*n+1
    senx=senx+signo*y**k/np.math.factorial(k)
    n=n+1
print("El valor aproximado de sen(",x,") es =",senx)


# In[ ]:




