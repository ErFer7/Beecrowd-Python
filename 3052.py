# -*- coding: utf-8 -*-

'''
Para resolver este problema são seguidos os seguintes passos:

1. É feita a leitura da matriz e para cada linha em que há prateleiras os seus inícios e fins são colocados
em uma lista. Isso significa que se uma prateleira começa em 2 e termina e 5 ela será registrada como [2, 5].
No fim dessa etapa a leitura está completa e há uma lista com as "coordenadas" das plataformas para cada linha.

2. É localizada a posição inicial da goteira.

3. 
'''

n, m = map(int, input().split())

c = []
prat_lst = []
a_lst = []
ap_lst = []

for i in range(n):

    ln = input()

    c.append(ln)

    ap_lst.append([])

    if i % 2 != 0:

        prat_lst.append([])

        in_prat = False
        prat_count = 0

        for j in range(m):

            if ln[j] == '#' and not in_prat:

                in_prat = True
                prat_lst[i].append([j])
                prat_count += 1
            elif ln[j] == '.' and in_prat:

                in_prat = False
                prat_lst[i][prat_count - 1].append(j - 1)
    else:

        prat_lst.append(None)

for i in range(m):

    if c[0][i] == 'o':

        a_lst.append([0, i])
        break

while len(a_lst) > 0:

    while a_lst[0][0] < n:

        if a_lst[0][1] not in ap_lst[a_lst[0][0]]:
            
            ap_lst[a_lst[0][0]].append(a_lst[0][1])

        if a_lst[0][0] < n - 1:

            if c[a_lst[0][0] + 1][a_lst[0][1]] == '#' or a_lst[0][1] in ap_lst[a_lst[0][0] + 1]:

                break

        a_lst[0][0] += 1

    a = a_lst[0]
    
    if a[0] % 2 == 0 and a[0] < n - 1:

        for p in prat_lst[a[0] + 1]:

            if a[1] >= p[0] and a[1] <= p[1]:

                for i in range(p[0], p[1] + 1):

                    if i not in ap_lst[a[0]]:

                        ap_lst[a[0]].append(i)

                if p[0] >= 1:

                    a_lst.append([a[0], p[0] - 1])
                
                if p[1] < m - 1:

                    a_lst.append([a[0], p[1] + 1])
    
    a_lst.remove(a_lst[0])

for i in range(n):

    ln = ""

    for j in range(m):

        if j in ap_lst[i]:

            ln += 'o'
        else:

            ln += c[i][j]
        
    c[i] = ln
    print(*c[i], sep = '')
