print(r"""
      
██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗████████╗ ██████╗ ███████╗███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔════╝██╔════╝
██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║   ██║   ██║   ██║███████╗███████╗
██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║   ██║   ██║   ██║╚════██║╚════██║
██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝   ██║   ╚██████╔╝███████║███████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝╚══════╝
      """)

def cadastrar_produtos():
    # Criar um dicionário para armazenar os produtos
    estoque = {}
    
    # Loop para cadastrar três produtos
    for i in range(3):
        nome_produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        
        # Adicionar o produto e a quantidade ao dicionário
        estoque[nome_produto] = quantidade
    
    return estoque

# Chamar a função para cadastrar produtos
estoque_final = cadastrar_produtos()

# Exibir o dicionário de produtos
print("Dicionário de produtos:", estoque_final)