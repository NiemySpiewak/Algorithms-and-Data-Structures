#Maja Sankowska
#Złożoność obliczeniowa: O(n^2)
#Złożoność pamięciowa: O(n^2)
#Rozwiązanie polaga na tym, że tworzymy tablicę max_komnat, w której zapisujemy największą liczbę komnat, 
#do której możemy dojść z danego pola oraz tablicę temp, w której zapisujemy możliwe liczby komnat, do których możemy dojść z danego pola.
#Następnie iterujemy po kolumnach i wierszach, sprawdzając, czy możemy przejść na dane pole, jeśli tak to sprawdzamy, 
#czy możemy przejść na to pole z lewej strony, z góry lub z dołu.

from zad7testy import runtests

def maze(L):

    n = len(L)
    
    if L[0][0] == '#' or L[n-1][n-1] == '#':
        return -1

    max_komnat = [[-float('inf')] * n for _ in range(n)]
    max_komnat[0][0] = 1 

    for i in range(1, n):
        if L[i][0] == '.':
            max_komnat[i][0] = max_komnat[i-1][0] + 1
        else:
            break

    for j in range(1, n):
        temp = [[-float('inf')] * 3 for _ in range(n)]
        
        for i in range(n):
            if L[i][j] == '.':
                if L[i][j-1] == '.':
                    temp[i][0] = max_komnat[i][j-1] + 1
                    
        for i in range(n):
            if L[i][j] == '.':
                if i > 0 and temp[i-1][1] != -float('inf'):
                    temp[i][1] = max(temp[i-1][1], temp[i-1][0]) + 1
                else:
                    temp[i][1] = temp[i][0]

        for i in range(n-1, -1, -1):
            if L[i][j] == '.':
                if i < n-1 and temp[i+1][2] != -float('inf'):
                    temp[i][2] = max(temp[i+1][2], temp[i+1][0]) + 1
                else:
                    temp[i][2] = temp[i][0]

        for i in range(n):
            if L[i][j] == '.':
                max_komnat[i][j] = max(temp[i])

    return max_komnat[n-1][n-1] - 1 if max_komnat[n-1][n-1] != -float('inf') else -1
    return 0

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
