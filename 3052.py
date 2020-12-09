# -*- coding: utf-8 -*-

'''
EM TESTES
'''

n, m = map(int, input().split())

c = []
ap_lst = []
a_lst = []

for _ in range(n):

    c.append(input())
    ap_lst.append([])

for i in range(m):

    if c[0][i] == 'o':

        a_lst.append((0, i))
        break

while len(a_lst) > 0:

    ap_lst[a_lst[0][0]].append(a_lst[0][1])

    a = a_lst[0]

    if a[0] < n - 1 and c[a[0] + 1][a[1]] != '#' and a[1] not in ap_lst[a[0] + 1]:

        a_lst.append((a[0] + 1, a[1]))

    if (a[0] < n - 1 and a[1] >= 1) and c[a[0] + 1][a[1]] == '#' and a[1] - 1 not in ap_lst[a[0]]:

        a_lst.append((a[0], a[1] - 1))
    
    if (a[0] < n - 1 and a[1] + 1 < m) and c[a[0] + 1][a[1]] == '#' and a[1] + 1 not in ap_lst[a[0]]:

        a_lst.append((a[0], a[1] + 1))
    
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
