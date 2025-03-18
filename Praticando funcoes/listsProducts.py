print(r"""
      
 _ _     _       
| (_)   | |      
| |_ ___| |_ ___ 
| | / __| __/ __|
| | \__ \ |_\__ \
|_|_|___/\__|___/
                 
                 

      """)

# Solicitar entrada do usuário
produtos_input = input("Digite os produtos separados por vírgula: ")
precos_input = input("Digite os preços separados por vírgula: ")

# Converter as entradas em listas
produtos = [produto.strip() for produto in produtos_input.split(',')]
precos = [preco.strip() for preco in precos_input.split(',')]

# Verificar se as listas têm o mesmo tamanho
if len(produtos) != len(precos):
    print("Erro: O número de produtos deve ser igual ao número de preços.")
else:
    # Exibir o resultado
    for produto, preco in zip(produtos, precos):
        print(f"{produto}: {preco}")