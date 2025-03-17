def palavras_comuns(texto1, texto2):
    # Remover pontuações e converter para minúsculas
    palavras1 = set(texto1.lower().split())
    palavras2 = set(texto2.lower().split())
    
    # Encontrar palavras em comum
    comuns = palavras1.intersection(palavras2)
    
    return comuns

# Exemplo de uso
texto1 = "O sol brilha forte no céu azul"
texto2 = "O céu azul anuncia um dia de sol intenso"

resultado = palavras_comuns(texto1, texto2)
print("Palavras em comum:", resultado)