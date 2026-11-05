def prix_billet(age):
    prix_billet = int(input("Veuillez saisir l'age du client: "))
    if prix_billet < 12:
        print(5)
    elif prix_billet >= 12 and <= 17:
        print(7)
    elif prix_billet >= 18 and <= 64:
        print(10)
    elif prix_billet >= 65:
        print(6)
    else:
        print("Veuillez saisir des informations corrects")
prix_billet(int(input("Saisit ton age: ")))