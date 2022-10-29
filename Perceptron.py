import time
import random
import numpy as np
from PIL import Image
from tkinter import messagebox
def imagen2vector():
    imagen0 = Image.open("A.jpg").convert(mode="L")
    imagen0_matriz = np.asarray(imagen0, dtype=np.uint8)
    vector1 = imagen0_matriz.flatten()
    
    imagen1 = Image.open("A1.jpg").convert(mode="L")
    imagen1_matriz = np.asarray(imagen1,dtype=np.uint8)
    vector2 = imagen1_matriz.flatten()
    
    imagen2 = Image.open("U.jpg").convert(mode="L")
    imagen2_matriz = np.asanyarray(imagen2,dtype=np.uint8)
    vector3 = imagen2_matriz.flatten()

    imagen3 = Image.open("U1.jpg").convert(mode="L")
    imagen3_matriz = np.asanyarray(imagen3,dtype=np.uint8)
    vector4 = imagen3_matriz.flatten()
    
    patrones = np.ones([4,401])
    
    for k in range(1,401):
        if vector1[k-1] == 255:
            patrones[0][k] = 1
        else:
            patrones[0][k] = -1

    for k in range(1,401):
        if vector2[k-1] == 255:
            patrones[1][k] = 1
        else:
            patrones[1][k] = -1
    
    for k in range(401):
        if vector3[k-1] == 255:
            patrones[2][k] = 1
        else:
            patrones[2][k] = -1

    for k in range(401):
        if vector4[k-1] == 255:
            patrones[3][k] = 1
        else:
            patrones[3][k] = -1
    
    P=4
    N=400

    return patrones,P,N     

def funct(x,m):
	if x >= 0:
		return 1
	
	elif x < 0:
		return -1

def modificacion(w,a,e,p):
	suma = 0
	for i in range(len(w)):
		w[i] = round(w[i]+(float(p[i])*float(a)*float(e)),4)

	return w

def y(w,pin,m):
	suma = 0

	for i in range(len(w)):
		suma += w[i]*pin[i]
	return (funct(suma,m))

def matriz_pesos(N):
	w = []
	repet = False
	i = 0
	while (i<N+1 and not(repet)):
		aux = round((random.uniform(-1, 1)),4)
		if aux in w:
			continue
		else:
			w.append(aux)
			i += 1
	return w
  
def mostrar_informacion(a,cont,alfa):
    a= str(round(a,4))
    cont = str(cont)
    alfa = str(alfa)
    messagebox.showinfo(message="Realizo "+cont+" iteraciones\nTiempo total:"+a+"s\nCon un alfa = "+alfa)

def proceso():
    patin,ent,N = imagen2vector()
    w = matriz_pesos(N)
    #ENTRADAS
    out = [1,1,-1,-1]#etiqueta de salida

    alfa = 0.05

    i = 0
    cont = 0
    fin = 0
    inicio = time.time()
    while((i != ent) and (int(fin-inicio) < 300)):
        fy = y(w,patin[i],-1)
        
        if ((out[i]-fy) == 0.0):
            i += 1
        else:
            cont += 1
            w = modificacion(w,alfa,out[i]-fy,patin[i])
            i = 0
            print(f"\nModificación #{cont}\nMatriz: {w}")

        if (i == ent):
            print(f"\nMatriz Óptima = {w}")
            break
        fin = time.time()
    if (int(fin-inicio) < 300):
        a=fin-inicio
        mostrar_informacion(a,cont,alfa)
    else:
        cont = str(cont)
        alfa = str(alfa)
        messagebox.showinfo(message="¡El programa tardó más de cinco minutos!\nRealizo "+cont+" iteraciones y un alfa de: "+alfa)
    opcion = 1
    while opcion == 1:
        fase_prueba(N,w)
        opcion = int(input("¿Desea probar otra imagen?  1=Si 2=No "))
    
def fase_prueba(N,w):
    N=N+1
    vector_prueba = np.ones([N])
    imagen_prueba = input("Ingrese la imagen de prueba:")
    imagen = Image.open(imagen_prueba).convert(mode="L")
    imagen_matriz = np.asanyarray(imagen,dtype=np.uint8)
    
    vector_imagen = imagen_matriz.flatten()
    #Paso mi imagen a vector y luego le aplico una funcion de tranferencia de 1 si =255 o -1 si = 0
    for k in range(1,401):
        if vector_imagen[k-1] == 255:
            vector_prueba[k] = 1
        else:
            vector_prueba[k] = -1

    
    fy = y(w,vector_prueba,-1)
    if fy == 1:
        print("Asocia con la letra A")
        messagebox.showinfo(message="La imagen de prueba: "+imagen_prueba+"se parece a la letra A")

    elif fy == -1:
        print("Asocia con la letra U")
        messagebox.showinfo(message="La imagen de prueba: "+imagen_prueba+" se parece a la letra U")

if __name__ == "__main__":
    proceso()