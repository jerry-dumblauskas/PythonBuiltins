lst1 = []
for a0 in range(10):
    for a1 in range(10):
        if a1 == a0:
            continue
        for a2 in range(10):
            if a2 in (a0, a1):
                continue
            for a3 in range(10):
                if a3 in (a0, a1, a2):
                    continue
                for a4 in range(10):
                    if a4 in (a0, a1, a2, a3):
                        continue
                    for a5 in range(10):
                        if a5 in (a0, a1, a2, a3, a4):
                            continue
                        for a6 in range(10):
                            if a6 in (a0, a1, a2, a3, a4, a5):
                                continue
                            for a7 in range(10):
                                if a7 in (a0, a1, a2, a3, a4, a5, a6):
                                    continue
                                for a8 in range(10):
                                    if a8 in (a0, a1, a2, a3, a4, a5, a6, a7):
                                        continue
                                    for a9 in range(10):
                                        if a9 in (a0, a1, a2, a3, a4, a5, a6, a7, a8):
                                            continue
                                        tmp = str(a0) + str(a1) + str(a2) + str(a3) + str(a4) + str(a5) + \
                                              str(a6) + str(a7) + str(a8) + str(a9)
                                        if int(tmp) % 10000000 == 0:
                                            print(tmp)
                                        if len(set(tmp)) == len(tmp):
                                            lst1.append(tmp)

tmp = sorted(list(set(lst1)))

for cnt, answer in enumerate(tmp):
    if cnt == 999999:
        print(answer)
