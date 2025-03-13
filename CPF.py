print(r"""
      
  ..|'''.|       '||''|.        '||''''|       
.|'     '         ||   ||        ||  .      || 
||                ||...|'        ||''|         
'|.      .        ||             ||         || 
 ''|....'        .||.           .||.           
                                               
                                               

      """)

import re

# Função para validar o CPF
def validar_cpf(cpf):
    # Define o padrão para o CPF no formato XXX.XXX.XXX-XX
    padrao_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    
    # Verifica se o CPF corresponde ao padrão
    if re.match(padrao_cpf, cpf):
        return True
    return False

# Solicita ao usuário que digite o CPF
cpf_cliente = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

# Chama a função para validar o CPF
if validar_cpf(cpf_cliente):
    print("O CPF está no formato correto.")
else:
    print("O CPF está no formato incorreto.")