montant_initial_de_linvestissement = 250000
taux_de_rendement_annuel = 0.02
Gain_annuel = montant_initial_de_linvestissement + taux_de_rendement_annuel*montant_initial_de_linvestissement
print(montant_initial_de_linvestissement)
print(taux_de_rendement_annuel)
print(Gain_annuel)

retrait_investisseur = 0.10 * Gain_annuel - 0.01 * Gain_annuel
print(retrait_investisseur)


