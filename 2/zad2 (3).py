#Maja Sankowska
#Tworzę tablice pomocniczą o rozmiarze p, tam przechowuje p elementów na których aktualnie pracuje. Pierwszym krokiem jest posortowanie tablicy, a nastepnie 
#wybieram k-ty największy element. Drugim krokiem jest usuwanie elementu i dodawanie kolejnego, szukam wartości i miejsca za pomocą binary searcha - w ten sposób 
#przesuwam się po całej tablicy i zliczam sume. 
#Złożoność czasowa: O(p log p + (n - p + 1) * (p + log p))
#Złożoność pamięciowa: O(n + p) 

from zad2testy import runtests

def ksum(T, k, p):

    def binary_search_for_val(T,x):

        l = 0
        r = p-1
        while l <= r:
            mid = (l+r)//2
            if T[mid] == x:
                return mid
            if T[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
    
    def binary_search_for_spot(T, x):

        l = 0
        r = p - 1
        while l < r:
            mid = (l+r)//2
            if T[mid] < x:
                l = mid + 1
            else:
                r = mid
        return l
    
    def dodajemy(T,x):
        T.insert(binary_search_for_spot(T,x),x)
    
    def usuwamy(T, x):
        del T[binary_search_for_val(T, x)]
    
    def sortujemy(T):
        if len(T) > 1:

            mid = len(T) // 2
            
            L = T[:mid]
            P = T[mid:]

            sortujemy(L)
            sortujemy(P)

            i = j = k = 0
            
            while i < len(L) and j < len(P):
                if L[i] <= P[j]:
                    T[k] = L[i]
                    i += 1
                else:
                    T[k] = P[j]
                    j += 1
                k += 1

            while i < len(L):
                T[k] = L[i]
                i += 1
                k += 1

            while j < len(P):
                T[k]=P[j]
                j += 1
                k += 1

    def ksum(T,k,p):
        suma = 0
        n = len(T)
        Tpom = T[:p]
        sortujemy(Tpom)
        for i in range (0,n-p+1):
            suma += Tpom[p-k]
            if i+p < n and T[i] != T[i+p]:
                usuwamy(Tpom,T[i])
                dodajemy(Tpom,T[i+p])
        return suma
    
    return ksum(T,k,p)
    return -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
