print(r"""
      
   ▄████████    ▄██████▄     ▄████████ ███▄▄▄▄   ████████▄     ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████ ███▄▄▄▄       ███      ▄██████▄     ▄████████ 
  ███    ███   ███    ███   ███    ███ ███▀▀▀██▄ ███   ▀███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄ ▀█████████▄ ███    ███   ███    ███ 
  ███    ███   ███    █▀    ███    █▀  ███   ███ ███    ███   ███    ███ ███   ███   ███   ███    █▀  ███   ███    ▀███▀▀██ ███    ███   ███    █▀  
  ███    ███  ▄███         ▄███▄▄▄     ███   ███ ███    ███   ███    ███ ███   ███   ███  ▄███▄▄▄     ███   ███     ███   ▀ ███    ███   ███        
▀███████████ ▀▀███ ████▄  ▀▀███▀▀▀     ███   ███ ███    ███ ▀███████████ ███   ███   ███ ▀▀███▀▀▀     ███   ███     ███     ███    ███ ▀███████████ 
  ███    ███   ███    ███   ███    █▄  ███   ███ ███    ███   ███    ███ ███   ███   ███   ███    █▄  ███   ███     ███     ███    ███          ███ 
  ███    ███   ███    ███   ███    ███ ███   ███ ███   ▄███   ███    ███ ███   ███   ███   ███    ███ ███   ███     ███     ███    ███    ▄█    ███ 
  ███    █▀    ████████▀    ██████████  ▀█   █▀  ████████▀    ███    █▀   ▀█   ███   █▀    ██████████  ▀█   █▀     ▄████▀    ▀██████▀   ▄████████▀  
                                                                                                                                                    
""")

# Função para processar as informações do paciente
def processar_informacoes(informacao):
    # Divide a string em partes usando ' - ' como delimitador
    partes = informacao.split(' - ')
    
    # Verifica se a entrada está no formato correto
    if len(partes) != 2:
        return None, None, None
    
    nome_completo = partes[0].strip()  # PrimeiroNome Sobrenome
    ano_nascimento = partes[1].strip()  # Ano

    # Divide o nome completo em primeiro nome e sobrenome
    nome_split = nome_completo.split()
    
    if len(nome_split) < 2:
        return None, None, None

    primeiro_nome = nome_split[0]  # Primeiro nome
    sobrenome = ' '.join(nome_split[1:])  # Sobrenome (pode ter mais de um)

    return primeiro_nome, sobrenome, ano_nascimento

# Solicita ao usuário que digite as informações do paciente
informacao_paciente = input("Digite o nome completo e o ano de nascimento do paciente: ")

# Chama a função para processar as informações
primeiro_nome, sobrenome, ano_nascimento = processar_informacoes(informacao_paciente)

# Exibe os resultados
if primeiro_nome and sobrenome and ano_nascimento:
    print(f"Primeiro Nome: {primeiro_nome}")
    print(f"Sobrenome: {sobrenome}")
    print(f"Ano de Nascimento: {ano_nascimento}")
else:
    print("Formato inválido! Certifique-se de usar o formato 'PrimeiroNome Sobrenome - Ano'.")