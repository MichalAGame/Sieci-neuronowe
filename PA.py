# -*- coding: utf-8 -*-
"""
Created on Mon May  1 20:58:23 2023

@author: Asus
"""

import numpy as np
import matplotlib as mp


def oblicz(arr,stala_uczenia,d):
    global w
    y=[0,0,0,0]    
    
    for i in range(len(y)):
        y[i]=funkcja_aktywacji(w.dot(arr[i]))
        w=w+stala_uczenia*(d[i]-y[i])*arr[i]        
    
    if y==d:
        return True
    else:
        return False
    
def And():
    return [0,0,0,1]
def Xor():
    return [0,1,1,0]

def funkcja_aktywacji(v):
    return 1 if v>0 else 0

def wykres_2D(arr,d):
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

    f=arr[0:4,1:2]
    g=arr[0:4,2:3]
    
    for i in range(len(arr)):
        if d[i]==1:
         mp.pyplot.scatter(f[i],g[i], marker='o',color='red')
        else:
         mp.pyplot.scatter(f[i],g[i], marker='o',color='blue')

    mp.pyplot.plot(a,b,color='red',linewidth=2,markersize=12)
    mp.pyplot.show()

def main():
    global w
    w=np.array([1/2,0,1])
    
    #And
    d = And()
    
    #Xor
    #d=Xor()
    
    arr = np.array([[1,  0,  0],
            [ 1, 0,  1],
            [ 1,  1,  0],
            [ 1, 1,  1]])
    
    stala_uczenia=1
    
    i = 0
    while i !=100:
        a=(oblicz(arr,stala_uczenia,d))
        wykres_2D(arr,d)
        i+=1
        if a:
            break
    
if __name__ == '__main__':
    main()