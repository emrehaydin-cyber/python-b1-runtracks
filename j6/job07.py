def f():
    L = [8, 24, 48, 2, 16]
    index = 0
    for i in L:
        if i % 3 == 0:
            index += 1
            print(index)
f()