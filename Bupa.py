# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt

def wykres2D_And(arr,d):
    c=w[0]
    x=w[1]
    y=w[2]
    
    a=[]
    b=[]
    if x!=0:
        a.append(-c/x)
        b.append(0)
        a.append(-(c+y)/x)
        b.append(1)
        
    if y!=0:
        a.append(0)
        b.append(-c/y)
        a.append(1)
        b.append(-(x+c)/y)
        
    e=arr[0:4,1:2]
    f=arr[0:4,2:3]
    for i in range(len(arr)):
        if d[i]==1:
         mp.pyplot.scatter(e[i],f[i], marker='o',color='red')
        else:
         mp.pyplot.scatter(e[i],f[i], marker='o',color='blue')
   
    mp.pyplot.plot(a,b,color='red',linewidth=2,markersize=12)
    mp.pyplot.show()
    
def wykres3D_Xor(arr,d):
    # Zakresy zmiennych
    x = np.linspace(0, 1, 10)
    y = np.linspace(0, 1, 10)
    X, Y = np.meshgrid(x, y)

    # Wyznaczenie wartości funkcji f w punktach (X,Y)
    Z = f(X, Y)

    # Tworzenie wykresu
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Rysowanie płaszczyzny
    ax.plot_surface(X, Y, Z, alpha=0.5)
    
    # Dodanie punktu  do wykresu
    e=arr[0:4,1:2]
    g=arr[0:4,2:3]
    h=arr[0:4,3:4]
    #print(arr[0:4,1:2])
    for i in range(len(arr)):
        if d[i]==1:
         ax.scatter(e[i], g[i], h[i], color='red')
        else:
         ax.scatter(e[i], g[i], h[i], color='blue')

    # Dodanie siatki
    ax.grid(True)

    # Ustawienie etykiet osi
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # Wyświetlenie wykresu
    plt.show()
    
def f(x, y):
    return (-w[1])*x + (-w[2])*y + w[3]

def oblicz(arr,stala_uczenia,d):
    global w
   
    y=[0,0,0,0]
    
    for i in range(len(arr)):
        y[i]=funkcja_aktywacji(w.dot(arr[i]))
        
    for i in range(len(arr)):
        w=w+stala_uczenia*(d[i]-y[i])*arr[i]
   
    if y==d:
        return True
    else:
        return False

def funkcja_aktywacji(v):
    return 1 if v>0 else 0

def And():
    return [0,0,1,0]

def arrAnd():
    return np.array([[1,  0,  0],
       [ 1, 0,  1],
       [ 1,  1,  0],
       [ 1, 1,  1]])

def Xor():
    return [0,1,1,0]

def arrXor():
    return np.array([[1,  0,  0,1],
        [ 1, 0,  1,1.66],
        [ 1,  1,  0,1.66],
        [ 1, 1,  1,1]])

def w_arr_xor():
    return np.array([1,0,1,1])


def main():
    global w
    
    #and
    #w=np.array([1,0,1])
    #d = And()
    #arr = arrAnd()
    
    #xor
    w=w_arr_xor()
    d=Xor()
    arr = arrXor()
    
    stala_uczenia=0.3
    
    
    i=1
    while i !=100:
        a=(oblicz(arr,stala_uczenia,d))
        
        #And
        #wykres2D_And(arr,d)
        
        #Xor
        wykres3D_Xor(arr,d)
        i+=1
        if a:
            break

if __name__ == '__main__':
    main()
    