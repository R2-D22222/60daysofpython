def palin(texto):
    texto = str(texto).replace(" ", "").lower()
    if texto == texto[::-1]:
        return f"{texto} É um palindromo"
    return f"{texto} Não é um palindrimo"

print(palin("ovo"))