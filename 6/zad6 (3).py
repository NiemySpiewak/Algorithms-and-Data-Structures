#Maja Sankowska
#Program wykorzystuje algorytm Dijkstry z dodatkową modyfikacją. Modyfikacja: zapisujemy odległości ze skokiem podwójnym i zwykłym krokiem.
#Nastęnie wybieramy krótszą drogę.
#Złożoność czasowa : V^3
from zad6testy import runtests
import heapq
def jumper( G, s, w ):
    # tu prosze wpisac wlasna implementacje
    n = len(G) 
    INF = float('inf')

    def skok(weight1, weight2):
        return max(weight1, weight2)
    
    odl = [[INF] * n for _ in range(2)]

    odl[0][s] = 0  
    odl[1][s] = 0  

    pq = [(0, s, 0)]   

    prev_vertex = [[] for _ in range(n)]

    while pq:
        o, u, krok = heapq.heappop(pq)
        if u==w: return o 
        if o > odl[0][u]:
            continue
        for v in range(n):
            if G[u][v] != 0:
                nowa_odl = INF
                for p in prev_vertex[u]:
                    if odl[0][p] + skok(G[u][v], G[p][u]) < nowa_odl:
                        nowa_odl = odl[0][p] + skok(G[u][v], G[p][u])
                    if nowa_odl < odl[1][v]:
                        odl[1][v] = nowa_odl
                        heapq.heappush(pq, (nowa_odl, v, 1))
                             
                nowa_odl = odl[krok][u] + G[u][v]
                if nowa_odl < odl[0][v] :
                    odl[0][v] = nowa_odl
                    heapq.heappush(pq, (nowa_odl, v, 0))
                    odl[1][v] = min(odl[1][v], nowa_odl)
                    prev_vertex[v].append(u)
                    
    return min(odl[0][w], odl[1][w])

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )


