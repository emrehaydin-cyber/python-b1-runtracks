def is_odd(c):
    if c > 0 and c % 1 == 0 and c % 2 == 0:
        print("c'est un nombre entier positif pair")
    elif c > 0 and c % 1 == 0 and c % 2 != 0:
        print("c'est un nombre entier positif impair")
    else:
        print("Veuillez saisir un entier positif !")
is_odd(176474747373773374747)