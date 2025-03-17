print(r"""
      
██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗███████╗ ██████╗ ██╗  ██╗██████╗ 
██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝██╔═══██╗██║  ██║██╔══██╗
██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ███████╗██║   ██║███████║██████╔╝
██║███╗██║██║   ██║██╔══██╗██╔═██╗ ╚════██║██║   ██║██╔══██║██╔═══╝ 
╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗███████║╚██████╔╝██║  ██║██║     
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     
                                                                    

      """)

def atualizar_estoque(estoque):
    # Solicitar o nome do produto a ser atualizado
    nome_produto = input("Nome do produto a ser atualizado: ")
    
    # Verificar se o produto existe no estoque
    if nome_produto in estoque:
        # Solicitar a nova quantidade
        nova_quantidade = int(input("Nova quantidade: "))
        
        # Atualizar a quantidade do produto
        estoque[nome_produto] = nova_quantidade
        
        print("Quantidade atualizada com sucesso!")
    else:
        print("Produto não encontrado no estoque.")
    
    return estoque

# Dicionário de estoque inicial
estoque = {
    "Caderno universitário": 50,
    "Caneta azul": 120,
    "Borracha branca": 30
}

# Chamar a função para atualizar o estoque
estoque_atualizado = atualizar_estoque(estoque)

# Exibir o dicionário de estoque atualizado
print(estoque_atualizado)