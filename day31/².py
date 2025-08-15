import math

def raiz_quadrada(numero):
    if numero < 0:
        raise ValueError("Coloque números positivos")
    return round(math.sqrt(numero), 2)
        
        
if __name__ == "__main__":
    print(raiz_quadrada(16))