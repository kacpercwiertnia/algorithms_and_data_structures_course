#Kacper Ćwiertnia
#
#Poniższy algorytm najpierw dokłada do Tablicy T w każdej krotce indeks budynku, a następnie 
#sortuję tablice T po 3 indeksie (wymiar b). Dla każdego budynku rozważam, że dany budynek buduję
#a następnie szukam najlepszego rozwiązania ze wszystkimi budynkami przed tym który aktualnie rozważam.
#Dzięki posortowaniu sprawdzanie nienachodzenia się budynków sprowadza się do porównania budynku, który
#aktualnie rozważam z tym który ostatnio wybudowałem. Poniższy Algorytm spamiętuję najlepsze rozwiązania
#dla każdego budynku przy danym ograniczeniu cenowym. Algorytm działa ponieważ rozważa wszystkie możliwe opcje.
#
#Złożoność obliczeniowa wynosi O(n^2*p) 

from zad4testy import runtests

def f(i, p, T, F, S):    
    if p - T[i][0][3] < 0:
        return 0

    if F[i][p][0] is None:
        flag = False
        maxi = 0
        ind = 0
        
        for j in range(i):
            if T[i][0][1] > T[j][0][2]:
                tmp = f(j, p-T[i][0][3], T, F, S)
                if tmp > maxi:
                    maxi = tmp
                    ind = j
                    flag = True
        
        if flag:
            F[i][p] = (maxi + S[i], ind, p-T[i][0][3])
        else:
            F[i][p] = (maxi + S[i], ind, 0)

    return F[i][p][0]

def printSol(T, F, p, i):
    A = [T[i][1]]
    nxt = (F[i][p][1], F[i][p][2])

    while F[nxt[0]][nxt[1]][1] is not None:
        A.append(T[nxt[0]][1])
        i = nxt[0]
        p = nxt[1]
        nxt = (F[i][p][1], F[i][p][2])

    A.sort()
    return A

def select_buildings(T,p):
    n = len(T)
    ind = 0
    F = [ [ (None,None,None) for _ in range(p+1) ] for i in range(n) ]
    
    for i in range(n):
        T[i] = (T[i], i)

    T = sorted(T, key=lambda x:(x[0][2], x[0][1]))

    S = [0 for _ in range(n)]
    for i in range(n):
        S[i] = T[i][0][0]*(T[i][0][2]-T[i][0][1])

    maxi = 0
    for i in range(n):
        maxi = max(maxi, f(i, p, T, F, S))

    for i in range(n):
        if F[i][p][0] == maxi:
            ind = i

    return printSol(T, F, p, ind)


runtests( select_buildings )
