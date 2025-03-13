import re

print(r"""
      
  _________                           .__               _______                 
 /   _____/ ____ _____ _______   ____ |  |__            \      \  __ __  _____  
 \_____  \_/ __ \\__  \\_  __ \_/ ___\|  |  \           /   |   \|  |  \/     \ 
 /        \  ___/ / __ \|  | \/\  \___|   Y  \         /    |    \  |  /  Y Y  \
/_______  /\___  >____  /__|    \___  >___|  /         \____|__  /____/|__|_|  /
        \/     \/     \/            \/     \/                  \/            \/ 

      """)

# Função para extrair o número da receita
def extrair_numero_receita(descricao):
    # Usa uma expressão regular para encontrar um número na descrição
    resultado = re.search(r'\d+', descricao)
    if resultado:
        return resultado.group()  # Retorna o número encontrado
    return None  # Retorna None se nenhum número for encontrado

# Solicita ao usuário que digite a descrição da receita
descricao_receita = input("Digite a descrição da receita: ")

# Chama a função para extrair o número da receita
numero_receita = extrair_numero_receita(descricao_receita)

# Exibe o resultado
if numero_receita:
    print(f"O número da receita é: {numero_receita}")
else:
    print("Nenhum número de receita encontrado.")