import random
import string

def gerador_de_senhas(tamanho):
    comprimeto = tamanho
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''
    
    while len(senha) < comprimeto:
        senha += random.choice(caracteres)
        
        print(f"Sua senha ficou assim: {senha}")
gerador_de_senhas(5)