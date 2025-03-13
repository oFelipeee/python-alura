print(r"""
      
'||'  '|'         '||   ||       '||                                        
 '|.  .'   ....    ||  ...     .. ||   ....     ....   ....     ...      || 
  ||  |   '' .||   ||   ||   .'  '||  '' .||  .|   '' '' .||  .|  '|.       
   |||    .|' ||   ||   ||   |.   ||  .|' ||  ||      .|' ||  ||   ||    || 
    |     '|..'|' .||. .||.  '|..'||. '|..'|'  '|...' '|..'|'  '|..|'       
                                                                            
                                                                            

      """)

# Função para validar o nome
def validar_nome(nome):
    # Verifica se o nome começa com letra maiúscula e contém apenas letras
    if nome.isalpha() and nome[0].isupper():
        return True
    return False

# Solicita ao usuário que digite o nome do cliente
nome_cliente = input("Digite o nome do cliente para validação: ")

# Chama a função para validar o nome
if validar_nome(nome_cliente):
    print("Nome válido!")
else:
    print("Nome inválido!")