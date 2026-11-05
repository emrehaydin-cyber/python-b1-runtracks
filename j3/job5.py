for i in range(2, 1001):
    if i >= 1 and i / 1 == i and i / i == 1 and all(i % e != 0 for e in range(2, i)):
        print(i)