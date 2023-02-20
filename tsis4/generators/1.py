def gene(dad):
    for i in range(dad):
        yield i**i


for i in gene(int(input())):
    print(i)