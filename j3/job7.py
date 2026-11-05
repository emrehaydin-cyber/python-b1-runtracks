pyr = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
nb_etage = 11
index = 0

for i in range(1, nb_etage + 1):
    nb_lettre = 2 * i - 1
    lettres = pyr[index : index + nb_lettre]
    index += nb_lettre
    espaces = " " * (nb_etage - i)
    print(espaces + lettres)
