a = int(input("entre la longueur pour le coté a: "))
b = int(input("entre la longueur pour le coté b: "))
c = int(input("entre la longueur pour le coté c: "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Pas possible de construire avec les longueurs fournit")
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Isocèle Rectangle")
elif a == b == c:
    print("Equilatéral")
elif a == b or a == c or b == c:
    print("Isocèle")
else:
    print("triangle quelconque")