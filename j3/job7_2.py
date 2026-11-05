pyr = "abcdefghijklmnopqrstuvwxyz" * 10
index = 0
i = 1
while index + (2 * i - 1) <= len(pyr):
    nb_lettre = 2 * i - 1
    lettres = pyr[index : index + nb_lettre]
    index += nb_lettre
    espaces = " " * (16 - i)
    print(espaces + lettres)
    i += 1