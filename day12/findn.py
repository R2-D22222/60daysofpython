def busli(lista, numeproco):
    for i, numero in enumerate(lista):
        if numero == numeproco:
            return i
    return -1

lista = [14, 24, 2, 1, 92]
numeproco = 1
busnum = busli(lista, numeproco)

if busnum != -1:
    print(f"o numero se encontra no indice: {busnum}")
else:
    print("numero não encontrado")
