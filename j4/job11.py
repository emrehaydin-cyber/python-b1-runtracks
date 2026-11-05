def time_to_text(nombre_entier):
    h = nombre_entier/60
    if nombre_entier > 0 and nombre_entier % 1 == 0:
        print(f"{nombre_entier} = {h - h%1}h et {(h % 1)*60} minutes") 
time_to_text(1234)
    