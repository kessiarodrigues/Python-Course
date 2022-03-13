def fatorial(n):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f

fat = int(input('Voce quer o fatorial de qual número? '))
print(fatorial(fat))
