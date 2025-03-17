print(r"""
       _______             __             __                          __           
|       \           |  \           |  \                        |  \          
| $$$$$$$\  ______  | $$  ______  _| $$_     ______    ______   \$$  ______  
| $$__| $$ /      \ | $$ |      \|   $$ \   /      \  /      \ |  \ /      \ 
| $$    $$|  $$$$$$\| $$  \$$$$$$\\$$$$$$  |  $$$$$$\|  $$$$$$\| $$|  $$$$$$\
| $$$$$$$\| $$    $$| $$ /      $$ | $$ __ | $$  | $$| $$   \$$| $$| $$  | $$
| $$  | $$| $$$$$$$$| $$|  $$$$$$$ | $$|  \| $$__/ $$| $$      | $$| $$__/ $$
| $$  | $$ \$$     \| $$ \$$    $$  \$$  $$ \$$    $$| $$      | $$ \$$    $$
 \$$   \$$  \$$$$$$$ \$$  \$$$$$$$   \$$$$   \$$$$$$  \$$       \$$  \$$$$$$ 
                                                                             
                                                                             
                                                                             
      """)

# Função para ler os produtos de um estoque e retornar como uma tupla
def ler_estoque(mensagem):
    produtos = input(mensagem)
    # Divide a string em uma lista e remove espaços em branco
    lista_produtos = [produto.strip() for produto in produtos.split(",")]
    # Converte a lista em uma tupla
    return tuple(lista_produtos)

# Lê os produtos dos dois estoques
estoque1 = ler_estoque("Produtos do estoque 1 (separados por vírgula): ")
estoque2 = ler_estoque("Produtos do estoque 2 (separados por vírgula): ")

# Combina os dois estoques em uma única tupla
estoque_combinado = estoque1 + estoque2

# Exibe o relatório com o estoque combinado
print("Estoque combinado:")
print(estoque_combinado)