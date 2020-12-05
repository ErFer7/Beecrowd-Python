# -*- coding: utf-8 -*-

check_state = 0

dp = {}
de = {}
dm = {}

n = int(input())

for _ in range(n):

    ln = input().split()

    dp[ln[0]] = int(ln[1])
    de[ln[0]] = int(ln[2])
    dm[ln[0]] = int(ln[3])

while True:

    keys = list(dp.keys())

    dp_values = list(dp.values())
    de_values = list(de.values())
    dm_values = list(dm.values())

    if check_state == 0:

        if dp_values.count(max(dp_values)) == 1:

            print(keys[dp_values.index(max(dp_values))])
            break
        else:

            for i in range(len(keys)):

                if dp_values[i] != max(dp_values):

                    del dp[keys[i]]
                    del de[keys[i]]
                    del dm[keys[i]]
    
    if check_state == 1:

        if de_values.count(max(de_values)) == 1:

            print(keys[de_values.index(max(de_values))])
            break
        else:

            for i in range(len(keys)):

                if de_values[i] != max(de_values):

                    del dp[keys[i]]
                    del de[keys[i]]
                    del dm[keys[i]]

    if check_state == 2:

        if dm_values.count(min(dm_values)) == 1:

            print(keys[dm_values.index(min(dm_values))])
            break
        else:
            
            print(min(filter(lambda s:isinstance(s, str), keys)))

            # for i in range(len(keys)):

            #     if dm_values[i] == min(dm_values):

            #         print(keys[i])
            #         break
            
            break

    check_state += 1