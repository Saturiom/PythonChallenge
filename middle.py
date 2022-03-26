list_m = []


def mid(b):
    middle = len(b)
    for x in b:
        list_m.append(x)
    if (middle % 2) == 1:
        midl = (middle // 2) + 1
        value = list_m[int(midl)-1]
        if list_m[int(midl)-1] == " ":
            print('Espace vide')
    else:
        value = "Mot paire"

    return print(value)


mid("Ji my")
