#Maja Sankowska
#Opis rozwiązania: tworzymy tablicę L o wymiarach n x m, gdzie n to długość listy X, a m to długość listy Y. 
# Wypełniamy ją wartościami inf. Wypełniamy pierwszy wiersz wartościami |X[0] - Y[j]|. 
# Następnie iterujemy po kolejnych wierszach i kolumnach, obliczając wartości w tablicy L. 
# Wartość w tablicy L[i][j] to minimum z wartości L[i-1][j-1] oraz wartości w kolumnie L[i][j-1]. Zwracamy wartość w tablicy - L[n-1][n-1:].
# Złożoność obliczeniowa: O(n*m)

from zad8testy import runtests

def parking(X, Y):
  n = len(X)
  m = len(Y)
  
  L = [[float('inf')] * m for _ in range(n)]
  
  for j in range(m):
      L[0][j] = abs(X[0] - Y[j])

  for i in range(1, n):
      min_val = float('inf')
      for j in range(i, m):
          min_val = min(min_val, L[i-1][j-1])
          L[i][j] = min_val + abs(X[i] - Y[j])
  
  return min(L[n-1][n-1:])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
