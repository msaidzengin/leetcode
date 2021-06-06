def metod(n):
    print(n)
    if n == 0:
        return
    metod(n - 1)

metod(5)