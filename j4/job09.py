def average(a,b,c):
    moyenne_etudiant = (a + b + c)/3
    if moyenne_etudiant >= 15:
        print(f"{moyenne_etudiant} : Très bon élève")
    elif moyenne_etudiant >= 11 and moyenne_etudiant <= 14:
        print(f"{moyenne_etudiant} : Bon élève")
    elif moyenne_etudiant >= 8 and moyenne_etudiant <= 10:
        print(f"{moyenne_etudiant} : élève moyen")
    elif moyenne_etudiant >= 0 and moyenne_etudiant <= 7:
        print(f"{moyenne_etudiant} : élève devant faire des efforts")
    else:
        print("Veuillez saisir 3 notes sur /20 !!!")
average(12,15,0) 