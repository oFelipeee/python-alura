# Programa de contagem regressiva para promoção de loja de livros

# Laço para contagem de 10 até 1
for i in range(10, 0, -1):
    if i % 2 == 0:  # Checa se o número é par
        print(f"Faltam apenas {i} segundos - Não perca essa oportunidade!")
    else:  # Se o número é ímpar
        print(f"A contagem continua: {i} segundos restantes.")

# Mensagem final após a contagem
print("Aproveite a promoção agora!")
