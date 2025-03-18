print(r"""
      
  __ _ _ _            
 / _(_) | |           
| |_ _| | |_ ___ _ __ 
|  _| | | __/ _ \ '__|
| | | | | ||  __/ |   
|_| |_|_|\__\___|_|   
                      
                      

      """)

def filtrar_pares(numeros):
    # Função que verifica se um número é par
    return list(filter(lambda x: x % 2 == 0, numeros))

# Solicitar entrada do usuário
entrada = input("Digite os números separados por espaço: ")

# Converter a entrada em uma lista de inteiros
numeros = list(map(int, entrada.split()))

# Filtrar os números pares
numeros_pares = filtrar_pares(numeros)

# Exibir o resultado
print("Números pares:", ' '.join(map(str, numeros_pares)))