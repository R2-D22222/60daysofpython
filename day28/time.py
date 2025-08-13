import time

def cronometro(tempo):
    print("iniciando cronômetro...")
    
    for segundo in range(tempo + 1):
        print(f"tempo: {segundo} segundos", end="\r" )
        time.sleep(1)
        
        print("\nCronometro finalizado")
        
        
if __name__ == "__main__":
    tempo = 10
    cronometro(tempo)
    