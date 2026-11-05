def my_long_world(a, b):
    for i in b:
        if len(i) > a:
            print(i)
my_long_world(3, ["je", "tu", "il", "elle", "nous", "vous", "ils"])