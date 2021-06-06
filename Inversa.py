#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
print("Programa que calcula la matriz inversa de una matriz dada de 2x2\n")
print("Ingreso de los datos de la matriz\n")
n=2 #Porque se trabaja con una matriz A de 2x2

#Definición de las matrices que empleo

matrizA=[]
matrizT=[]
matrizAdj=[]
matrizA_Inversa=[]
det=0 #Variable dónde se almacenará el valor del determinante de la matriz A

#Llenado inicial de las matrices con ceros

for i in range(n):
    matrizA.append([0]*n)
    matrizT.append([0]*n)
    matrizAdj.append([0]*n)
    matrizA_Inversa.append([0]*n)

#Ingreso de datos en la matriz A mediante teclado

for i in range(n):
    #print(i)
    for j in range(n):
        matrizA[i][j]=float(input(" Digite el dato de la fila {}, columna {} : ".format(i+1,j+1)))
        
det=np.linalg.det(matrizA) #Cálculo del determinante de la matriz A haciendo uso de numpy
#print(det)

#Cálculo de la matriz inversa

if det!=0:
    for i in range(n):
        for j in range(n):
            matrizT[i][j]=matrizA[j][i] #Matriz transpuesta de nuestra matriz A
    for i in range(n):
        for j in range(n):
            matrizAdj[i][j]=[((-1)**(i+j))*matrizT[1-i][1-j]] #Matriz adjunta de nuestra matriz A transpuesta
            #print(matrizA[i][j],matrizT[i][j],matrizAdj[i][j])
            matrizA_Inversa[i][j]=matrizAdj[i][j]/det
    print("\n\tLa matriz invertida es\n")
    for i in range(n):
        for j in range(n):
            print("\t",matrizA_Inversa[i][j],end="")
        print("\n")
else: print("\nLa matriz dada no es invertible")


# In[ ]:




