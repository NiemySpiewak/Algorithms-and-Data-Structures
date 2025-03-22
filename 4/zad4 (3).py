# Maja Sankowska
# Program bazuje na algorytmie DFS oraz używa list sąsiedztwa. Przechodząc po grafie badamy ścieżki, które nie mają
# większej róznicy niż 2t + 1, co oznacza że samolot da radę przelecieć.
# Złożoność: V!

from zad4testy import runtests

def Flight(L,x,y,t):

    def rep_grafu(krawedzie):
    
        lista= {}

        for krawedz in krawedzie:
            start, koniec, waga = krawedz
            if start not in lista:
                lista[start] = []
            if koniec not in lista:
                lista[koniec] = []
            lista[start].append((koniec, waga))
            lista[koniec].append((start, waga))
        return lista

    def dfs(graf, wskaznik, koniec, visited, min_waga, max_Waga, t):
      
      if wskaznik == koniec:
          return True

      visited[wskaznik] = True

      for sasiad, waga in graf[wskaznik]:
          if not visited[sasiad]:
              min_sasiad_waga = min(min_waga, waga)
              max_sasiad_waga = max(max_Waga, waga)
              if max_sasiad_waga - min_sasiad_waga <= 2*t:
                  if dfs(graf, sasiad, koniec, visited, min_sasiad_waga, max_sasiad_waga, t):
                      return True

      visited[wskaznik] = False
      return False

    def zadanie(graf, start, koniec, t):
        visited = {node: False for node in graf} 
        return dfs(graf, start, koniec, visited, float('inf'), float('-inf'), t)


    return zadanie(rep_grafu(L), x, y, t)

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
