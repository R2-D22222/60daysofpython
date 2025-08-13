def write_file(nanmef, conteudo):
    with open(nanmef, "w") as file:
        file.write(conteudo)
        
        print(f"O conteudo foi salvo em: {nanmef}")
def read_file(nanmef):
    
    try:
        with open(nanmef, "r") as file:
            conteudo = file.read()
        print(f"Conteudo do arquivo: {conteudo}")
    except FileNotFoundError:
        print("Não foi possivel encontrar o arquivo")
        
def main(nanmef, conteudo):
    
    print("Seja bem vindo ao programa de leitura e escrita de arquivos")
    
    
    write_file(nanmef, conteudo)
    
    print("fazendo a leitura do arquivo")
    read_file(nanmef)
    
    
if __name__ == "__main__":
        file = "exemplo.txt"
        texto = "Artorias, walker of the abyss"
        
        main(file, texto) 
        
        