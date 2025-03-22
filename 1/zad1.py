# Maja Sankowska
# Kod wykonuje merge sorta na listach odsyłaczowych. Składa się z trzech funkcji: znajdującej środek listy, merga i margesorta. 
# Złożoność czasowa dla k = Θ(1): O(nlogn)
# Złożoność czasowa dla k = Θ(log n): O(nlogn)
# Złożoność czasowa dla k = Θ(n): O(nlogn)


from zad1testy import Node, runtests

def SortH(p,k):

    def znajdz_srodek(p):
        if p == None: return None
        wskaznik_w = p
        wskaznik_s = p
        while wskaznik_s.next != None and wskaznik_s.next.next != None:
            wskaznik_s = wskaznik_s.next.next
            wskaznik_w = wskaznik_w.next
        return wskaznik_w

    def mergesort(p):

        if p is None or p.next is None:
            return p
        
        koniec1 = znajdz_srodek(p)
        pocz2 = koniec1.next
        koniec1.next = None

        pierwsza_polowa = mergesort(p)
        druga_polowa = mergesort(pocz2)

        return merge(pierwsza_polowa, druga_polowa)

    def merge(pierwsza_polowa,druga_polowa):

        lista1 = Node()
        wynik = lista1
        wskaznik_1 = pierwsza_polowa
        wskaznik_2 = druga_polowa

        while wskaznik_1 != None and wskaznik_2 != None:
            if wskaznik_1.val < wskaznik_2.val:
                lista1.next = wskaznik_1
                wskaznik_1 = wskaznik_1.next
            else:
                lista1.next = wskaznik_2
                wskaznik_2 = wskaznik_2.next       
            lista1 = lista1.next

        while wskaznik_1 != None:
            lista1.next = wskaznik_1
            wskaznik_1 = wskaznik_1.next
            lista1 = lista1.next
        while wskaznik_2 != None:
            lista1.next = wskaznik_2
            wskaznik_2 = wskaznik_2.next
            lista1 = lista1.next
            

        return wynik.next
        
    return mergesort(p)

    pass

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
