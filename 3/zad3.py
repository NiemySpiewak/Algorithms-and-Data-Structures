#Maja Sankowska
#Algorytm iteruje po wszystkich największych y. I dla każdego z nich wykonuje:
#zlicza wszystkie punkty ponad punktem
#zlicza wszystkie punkty po prawej od punktu
#odejmuje od wszystkich punktów te po prawej i te powyżej 
#w ten sposób dostajemu liczeb punktów zdominowanych przed dany punkt

from zad3testy import runtests

def dominance(P):

    def counting_sort_x(arr):
        max_x = max(arr, key=lambda x: x[0])[0]
        max_y = max(arr, key=lambda x: x[1])[1]

        count_y = [0] * (max_y + 1)

        for tup in arr:
            count_y[tup[1]] += 1

        for i in range(1, max_y + 1):
            count_y[i] += count_y[i - 1]
        result = [None] * len(arr)

        for tup in reversed(arr):
            y_index = count_y[tup[1]] - 1
            result[y_index] = tup
            count_y[tup[1]] -= 1
        count_x = [0] * (max_x + 1)

        for tup in result:
            count_x[tup[0]] += 1

        for i in range(1, max_x + 1):
            count_x[i] += count_x[i - 1]
        final_result = [None] * len(arr)

        for tup in reversed(result):
            x_index = count_x[tup[0]] - 1
            final_result[x_index] = tup
            count_x[tup[0]] -= 1

        return final_result

    def counting_sort_y(arr):

        max_value = max(arr, key=lambda x: x[1])[1]
        min_value = min(arr, key=lambda x: x[1])[1]
        
        count = [0] * (max_value - min_value + 1)
        
        for tup in arr:
            count[tup[1] - min_value] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        output = [None] * len(arr)

        for tup in reversed(arr):
            output[count[tup[1] - min_value] - 1] = tup
            count[tup[1] - min_value] -= 1
        
        return output

    n=len(P)

    for i in range (n):
        P[i] = P[i][0]-1,P[i][1]-1



    posortowane_y = counting_sort_y(P)
    
    above = (n+1) * [0]
    cnty = 1
    for i in range (n-1):
        if posortowane_y[i][1] != posortowane_y[i+1][1]:
            above[posortowane_y[i][1]] = cnty
            cnty = 1
        else:
            cnty += 1

    above[posortowane_y[n-1][1]] = cnty

    for i in range (n-1,-1,-1):
        above[i] = above[i] + above[i+1]

    posortowane_x = counting_sort_x(P)

    right = (n+1) * [0]
    cntx = 1
    for i in range (n-1):
        if posortowane_x[i][0] != posortowane_x[i+1][0]:
            right[posortowane_x[i][0]] = cntx
            cntx = 1
        else:
            cntx += 1
    
    right[posortowane_x[n-1][0]] = cntx

    ile_pkt_w_kolumnie = right.copy()

    for i in range (n-1,-1,-1):
        right[i] = right[i] + right[i+1]



    pkt_zew = n * [0]

    for i in range(n-1):
        if posortowane_x[i][1] != posortowane_x[i+1][1]:
            pkt_zew[posortowane_x[i][0]] = posortowane_x[i][1]
    pkt_zew[posortowane_x[n-1][0]] = posortowane_x[n-1][1]
    
    wartosc = 0
    for i in range (n):
        temp = 0
        if ile_pkt_w_kolumnie[i] > 0:
            temp = n - above[pkt_zew[i]] - right[i] + 1
        wartosc = max(temp,wartosc) 

    return wartosc

    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
