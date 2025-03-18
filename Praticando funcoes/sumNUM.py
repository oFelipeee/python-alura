print(r"""
      
                                                 
                                                 
 _ __  _   _ _ __ ___  ___   ___ _   _ _ __ ___  
| '_ \| | | | '_ ` _ \/ __| / __| | | | '_ ` _ \ 
| | | | |_| | | | | | \__ \ \__ \ |_| | | | | | |
|_| |_|\__,_|_| |_| |_|___/ |___/\__,_|_| |_| |_|
                                                 
                                                 

      """)
def soma_recursiva(n):
    # Caso base: se n for 1, retorna 1
    if n == 1:
        return 1
    # Chamada recursiva: soma o número atual com a soma dos números anteriores
    return n + soma_recursiva(n - 1)

# Solicitar entrada do usuário
n = int(input("Digite um número: "))

# Calcular a soma de 1 até n
resultado = soma_recursiva(n)

# Exibir o resultado
print(f"A soma de 1 a {n} é: {resultado}")
