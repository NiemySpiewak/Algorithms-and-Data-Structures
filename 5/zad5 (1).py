#Maja Sankowska
#Program pierwsze co robi to reprezentuje graf w formie listy sąsiedztwa (łącznie z osobliwościami). Następnie wykonuje 
#algorytm dijkstry, tym znajdując trase z najszybszym czasem.
#Złożoność: V^2

from zad5testy import runtests
import queue

def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje

    def rep_grafu(krawedzie,n,osobliwosci):
        lista = [[] for _ in range(n)]

        for krawedz in krawedzie:
            start, koniec, waga = krawedz
            lista[start].append((koniec, waga))
            lista[koniec].append((start, waga))
        for i in range(len(osobliwosci)):
            for j in range(i + 1, len(osobliwosci)):
                v1 = osobliwosci[i]
                v2 = osobliwosci[j]
                lista[v1].append((v2, 0))
                lista[v2].append((v1, 0))
        return lista
    
    def dijkstra(graf, start, koniec, n):
    
        odleglosci = [float('inf')] * n
        odleglosci[start] = 0

        q = queue.PriorityQueue()
        q.put((0, start))

        while not q.empty():
            curr_odl, curr_wiesz = q.get()

            if curr_wiesz == koniec:
                return odleglosci[koniec]

            if curr_odl > odleglosci[curr_wiesz]:
                continue

            for sasiad, czas in graf[curr_wiesz]:
                odleglosc = curr_odl + czas
                if odleglosc < odleglosci[sasiad]:
                    odleglosci[sasiad] = odleglosc
                    q.put((odleglosc, sasiad))
        return None
    return dijkstra(rep_grafu(E,n,S),a,b,n)
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )