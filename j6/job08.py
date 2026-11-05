def f():
    l = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    nb_pair = 0
    for i in l:
        if i % 2 == 0:
            nb_pair = nb_pair + i
            print(nb_pair)
        else:
            pass
f()