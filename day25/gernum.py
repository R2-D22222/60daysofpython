import random

def gerador_de_numeros_aleatorios():
    print("Bem vindo ao gerador de numeros aleatórios")
    
    numran = []
    
    for _ in range(10):
        numero = random.randint(1, 100)
        numran.append(numero)
        
    print(f"numeros aleatorios são: ")
    for i, numero in enumerate(numran, start=1):
            print(f"numero {i} = {numero}")
            
if __name__ == "__main__":
    gerador_de_numeros_aleatorios()        