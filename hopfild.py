import numpy as np
import matplotlib

def inicjalizacjia():
    global aktywacja
    global punkty_stabilne_odswiezanie_asyn
    global cykl_odswiezanie_asyn
    global punkty_stabilne_odswiezanie_syn
    global cykl_odswiezanie_syn
    
    aktywacja=0
    punkty_stabilne_odswiezanie_asyn=[]
    cykl_odswiezanie_asyn=[]
    
    punkty_stabilne_odswiezanie_syn=[]
    cykl_odswiezanie_syn=[]

def warunki_stabilizacji(matrix):
    return diagon(matrix) & function(matrix)

def diagon(matrix):
    l = np.diag(matrix)
    s = l<0
    l = len(l[s])==0

    return l

def function(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[i][j]!=matrix[j][i]):
                return False
    return True

def czy_macierz_dodatnio_okreslona(arr):
    
    b=arr>0
    if not b.all():
        return False
    
    if np.linalg.det(arr)<=0:
        return False
    
    for i in range(3):
        for j in range(3):
            a=np.delete(arr, i, 1)
            a=np.delete(a, j, 0)
            if np.linalg.det(a)<=0:
                return False
    return True

def odswiezanie_asynchroniczne(matrix,x1):
    arr=[]
    
    maxiteration=4
    if len(matrix) == 3:
        maxiteration=9
        
    j=1;
    while j<=maxiteration:
        for i in range(len(matrix)):
            v=np.dot(matrix[i],x1)
            x1[i]=funkcja_aktywacji(v)
        j+=1
        if x1 in arr:
            break
        else:
            arr.append(x1)

    punkt_stabilny_odswiezanie_asyn(arr)
    
def odswiezanie_synchroniczne(matrix,x1):
    v=np.dot(matrix,x1)
    arr=[]
    
    maxiteration=4
    if len(matrix) == 3:
        maxiteration=9
    
    j=1;
    while j<=maxiteration:
        for i in range(len(matrix)):
            x1[i]=funkcja_aktywacji(v[i])
        j+=1
        if x1 in arr:
            break
        else:
            arr.append(x1)

    punkt_stabilny_odswiezanie_syn(arr)
    
    
def funkcja_aktywacji(v):
    return 1 if v>aktywacja else -1

def punkt_stabilny_odswiezanie_asyn(arr):
    if len(arr)==1:
        if arr[0] not in punkty_stabilne_odswiezanie_asyn:
            punkty_stabilne_odswiezanie_asyn.append(arr[0])
    else:
        if arr not in cykl_odswiezanie_asyn:
          cykl_odswiezanie_asyn.append(arr)
        
def punkt_stabilny_odswiezanie_syn(arr):
    if len(arr)==1:
        if arr[0] not in punkty_stabilne_odswiezanie_syn:
              punkty_stabilne_odswiezanie_syn.append(arr[0])
    else:
        if arr not in cykl_odswiezanie_syn:
         cykl_odswiezanie_syn.append(arr)
        
def wyswietlenie_punktow_stabilnych_asyn():
    print("punkty stale - odswiezanie asynchroniczne")
    print(punkty_stabilne_odswiezanie_asyn)
    
def wyswietlenie_punktow_stabilnych_syn():
    print("punkty stale - odswiezanie synchroniczne")
    print(punkty_stabilne_odswiezanie_syn)
    
def wyswietlenie_cykli_asyn():
    print("cykl - odswiezanie asynchroniczne")
    print(cykl_odswiezanie_asyn)
    
def wyswietlenie_cykli_syn():
    print("cykl - odswiezanie synchroniczne")
    print(cykl_odswiezanie_syn)
    
def main():
    inicjalizacjia()
    
    aktywacja = 0
    
    #matrix = [[0,  1],[1,  0]]
    
    #wektor = [[1,  1],[1,  -1],[-1,  1],[-1,  -1]]
    
    matrix = [[0,  -2/3,  2/3],
            [ -2/3, 0,  -2/3],
            [ 2/3,  -2/3,  0]]
    
    wektor = [[1,  -1,  1],
          [-1,  1,  -1],
          [1,  1,  1],
          [-1,  1,  1],
          [1,  1,  -1],
          [-1,  -1,  -1],
          [-1,  -1,  1],
          [1,  -1,  -1]]
    
    warunki_stabilizacji_=warunki_stabilizacji(matrix)
    if warunki_stabilizacji_:
        print("Mamy pewność, że sieć Hopfielda w trybie asynchronicznym ustabilizuje się na punkcie stałym")
    else:
        print("Nie mamy pewności, że sieć Hopfielda w trybie asynchronicznym ustabilizuje się na punkcie stałym")
        
    for i in range(len(wektor)):
        odswiezanie_asynchroniczne(matrix,wektor[i])
    wyswietlenie_punktow_stabilnych_asyn()    
    wyswietlenie_cykli_asyn()
    
    czy_dodatnio_okreslona=czy_macierz_dodatnio_okreslona(np.array(matrix))
    if warunki_stabilizacji_ and czy_dodatnio_okreslona:
        print("Maciez jest dodatnio okreslona. Mamy pewność, że sieć Hopfielda w trybie synchronicznym ustabilizuje się na punkcie stałym")
    elif warunki_stabilizacji_ and not czy_dodatnio_okreslona:
        print("Maciez jest ujemnie okreslona. Siec ustabilizuje się na punkcie stałym lub na dwuokresowej konfiguracji")
        
    for i in range(len(wektor)):
        odswiezanie_synchroniczne(matrix,wektor[i])
  
    wyswietlenie_punktow_stabilnych_syn()
    wyswietlenie_cykli_syn()
    
if __name__ == '__main__':
    main()