import numpy as np
print("Programa que calcula la matriz inversa de una matriz dada de 2x2")
print("Ingreso de los datos de la matriz")
n=2
matrizA=[]
matrizT=[]
matrizAdj=[]
matrizA_Inversa=[]
Aux=[0]
det=0
for i in range(n):
    matrizA.append([0]*n)
    matrizT.append([0]*n)
    matrizAdj.append([0]*n)
    matrizA_Inversa.append([0]*n)
for i in range(n):
    #print(i)
    for j in range(n):
        matrizA[i][j]=float(input(" Digite el dato de la fila {}, columna {} : ".format(i+1,j+1)))
det=np.linalg.det(matrizA)
#print(det)
if det!=0:
    for i in range(n):
        for j in range(n):
            matrizT[i][j]=matrizA[j][i] #Matriz transpuesta de nuestra matriz A
    for i in range(n):
        for j in range(n):
            matrizAdj[i][j]=[((-1)**(i+j))*matrizT[1-i][1-j]] #Matriz adjunta de nuestra matriz A transpuesta
            #print(matrizA[i][j],matrizT[i][j],matrizAdj[i][j])
            matrizA_Inversa[i][j]=(matrizAdj[i][j]/det)
    for i in range(n):
        for j in range(n):
            print("\t",matrizA_Inversa[i][j],end="")
        print("\n")
else: print("La matriz dada no es invertible")
