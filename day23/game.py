import random

def jogo_adivinhaçao():
    print("try your luck")
    
    nsecret = random.randint(0, 10)
    
    tentativas = 0
    
    while True:
        try:
            palpite = int(input("Tente acertar: "))
            tentativas +=1
            
            if palpite < nsecret:
                print("Errado, muito abaixo")
            elif palpite > nsecret:
                print("Errado, muito acima")
            else:
                print(f"Parabéns vc acertou, o número era: {nsecret} e suas tentativas foram {tentativas}")
                break
            
        except ValueError:
            print("Digite um número inteiro")
            
if __name__ == "__main__":
    jogo_adivinhaçao()  
        
        