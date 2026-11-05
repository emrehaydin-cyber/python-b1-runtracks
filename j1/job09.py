nom_du_produit = " ordinateur portable "
prix_unitaire = 100
quantité_en_stock = 19

print("=" * 40)
print(f" Nom du produit   : {nom_du_produit.strip().capitalize()}")
print(f" Prix unitaire    : {prix_unitaire:.2f} €")
print(f" Quantité en stock: {quantité_en_stock} unités")
print("=" * 40)

quantité_souhaitée = int(input("\nselectionnez le nombre de pc que vous souhaitez : "))
quantité_en_stock = quantité_en_stock - quantité_souhaitée
prix_unitaire = prix_unitaire * 1.10

print(quantité_souhaitée)
print(quantité_en_stock)
print(prix_unitaire)
