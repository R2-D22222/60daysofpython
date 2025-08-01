def anagrama(palavra1, palavra2):
        
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()
    
    if sorted(palavra1) == sorted(palavra2):
        return f"essas palavras são anagramas"
    return f"essas palavras nao são anagramas"
print(anagrama("sith", "lord"))