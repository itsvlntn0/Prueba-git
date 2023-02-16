import numpy as np

#arreglo = np.array([[10,10,10],[20,20,20],[30,30,30]])
#print(arreglo)

#arreglo = np.array([[10,10,10],[20,20,20],[30,30,30]])
#print(sum(arreglo)) suma las columnas
#print(np.sum(arreglo)) suma el arreglo

#Primero filas segundo columnas
"""arr = np.zeros([8,4])

for f in range (8):
    for c in range(4):
        numero=int(input("Digite un numero: "))
        arr[f,c]=numero
print(arr)"""

arr = np.ones([4,3])

for f in range (4):
    for c in range(3):

        repeticion = True

        while(repeticion):
            numero=int(input("Digite un numero: "))

            if(numero %2 == 0):
                arr[f,c]= numero
                repeticion = False
    
        
print(arr)

