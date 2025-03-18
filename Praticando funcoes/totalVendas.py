print(r"""
      
                     _           
                    | |          
__   _____ _ __   __| | __ _ ___ 
\ \ / / _ \ '_ \ / _` |/ _` / __|
 \ V /  __/ | | | (_| | (_| \__ \
  \_/ \___|_| |_|\__,_|\__,_|___/
                                 
                                 

      """)

def calcular_total_vendas(vendas):
    # Converte a string de vendas em uma lista de números
    lista_vendas = map(float, vendas.split())
    # Calcula o total
    total = sum(lista_vendas)
    return total

# Solicitar entrada do usuário
entrada = input("Digite os valores das vendas: ")

# Calcular o total de vendas
total_vendas = calcular_total_vendas(entrada)

# Exibir o resultado
print(f"O total de vendas foi: {total_vendas}")