def arr(a, b):
    l_ar=[]
    for nb in a:
        l_ar.append(round(nb, b))
    l_t=sorted(l_ar)
    print(l_t)
arr([22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50], 0)