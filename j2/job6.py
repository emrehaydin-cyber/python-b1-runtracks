N = int(input("Entrez l'entier N : "))
nb_resultats = int(input("Combien de résultats souhaitez-vous afficher ? "))

i = 1

while i <= nb_resultats:
    resultat = i * N * 7
    print(f"{i} × {N} × 7 = {resultat}")
    i += 1

