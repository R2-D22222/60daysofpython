def contador():
    try:
        limit = int(input("Digite o número de sua escolha: "))
        limit = limit + 1
        for i in range(limit):
            print(i)
            
            if i == limit:
                print("O contador atingiu ao número máximo")
                break
            
    except ValueError:
        print("Erro. Por favor, insira um número inteiro")
        
contador()