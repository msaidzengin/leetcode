def metod(n):
    print(n)
    if n > 100:
        return
    metod(n + n)

metod(1)
