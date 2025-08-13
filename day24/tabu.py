def tabuada():
    try:
        numero = int(input("Digite o numero que desejas: "))
        
        print(f"\n tabuada de {numero}: ")
       
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
        
    except ValueError:
        print("Somente números inteiros")
        
if __name__ == "__main__":
     tabuada()