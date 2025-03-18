print(r"""
      
 _     _           _      
(_)   | |         | |     
 _  __| | __ _  __| | ___ 
| |/ _` |/ _` |/ _` |/ _ \
| | (_| | (_| | (_| |  __/
|_|\__,_|\__,_|\__,_|\___|
                          
                          

      """)

def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade

# Solicitar entrada do usuário
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

# Calcular a idade
idade = calcular_idade(ano_nascimento, ano_atual)

# Exibir o resultado
print(f"A idade é {idade} anos.")