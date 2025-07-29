def fatorial(n):
    if n < 0:
        raise ValueError("Somente números positivos")
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n -1)

try:
    n = int(input("Digite o numero que deseja fatoriar: "))
    print(fatorial(n))
except ValueError as A:
    print(A)