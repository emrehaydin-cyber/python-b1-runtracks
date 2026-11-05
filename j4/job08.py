def what_to_eat(type, season):
    if type == "Fruits" and season == "Hiver":
        print("orange, mandarine et kiwi")
    elif type == "Fruits" and season == "été":
        print("Poire,fraise cassis")
    elif type == "Légumes" and season == "Hiver":
        print("Carotte,topinambour, endive")
    elif type == "Légumes" and season == "été":
        print("artichaut, aubergine, navet")
    else:
        print("Erreur fruitière !")
what_to_eat("Fruits", "Hiver")