liste_w = []
liste_tmp = []
liste_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def capital_indexes(a):
    tmp = 0
    for x in a:
        if x in liste_upper:
            liste_w.append(tmp)
            liste_tmp.append(x)
            tmp += 1

        else:
            tmp += 1

    print(liste_tmp)

    return print(liste_w)


capital_indexes("DouGLaS")
