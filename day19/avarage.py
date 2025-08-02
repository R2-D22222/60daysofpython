def media(notas):
    media = sum(notas) / len(notas)
    
    return round(media, 2)

print(media([10, 9, 8, 2, 4]))