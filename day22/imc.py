def calcular_imc():
    
    print("Seja bem vindo a calculadora de imc")
    
    try:
        peso = float(input("Digite o seu peso: "))
        altura = float(input("Digite a sua altura: "))
        
        if peso < 0 or altura < 0:
         print("O seu peso e altura precisa ser maior que 0")
         return
        
        imc = round(peso / (altura **2), 2)
        
        if imc < 18.5:
            print("Você está abaixo do peso")
        elif 18.5 <= imc <29.9:
            print("Seu peso está normal")
        elif 25 <= imc < 29.9:
            print("Você está com sobrepeso")          
        else:
            print("Você está obeso")
    except ValueError:
        print("Entrada inválida")
        
if __name__ == "__main__":
    calcular_imc()
        
        
        
        
    