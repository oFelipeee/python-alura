print(r"""                                                                           
 ______  ______  ______  ______  ______  ______  ______  ______  ______  ______ 
|      \|      \|      \|      \|      \|      \|      \|      \|      \|      \
 \$$$$$$ \$$$$$$ \$$$$$$ \$$$$$$ \$$$$$$ \$$$$$$ \$$$$$$ \$$$$$$ \$$$$$$ \$$$$$$                                                                                                                                                                                                                                                                                                     
________  ______  __    __  ________  _______                                  
|        \|      \|  \  |  \|        \|       \                                 
| $$$$$$$$ \$$$$$$| $$  | $$| $$$$$$$$| $$$$$$$\                                
| $$__      | $$   \$$\/  $$| $$__    | $$  | $$                                
| $$  \     | $$    >$$  $$ | $$  \   | $$  | $$                                
| $$$$$     | $$   /  $$$$\ | $$$$$   | $$  | $$                                
| $$       _| $$_ |  $$ \$$\| $$_____ | $$__/ $$                                
| $$      |   $$ \| $$  | $$| $$     \| $$    $$                                
 \$$       \$$$$$$ \$$   \$$ \$$$$$$$$ \$$$$$$$                                                                                                              
 \$$$$$$ \$$$$$$ \$$$$$$ \$$$$$$ \$$$$$$ \$$$$$$ \$$$$$$ \$$$$$$ \$$$$$$ \$$$$$$
      """)

# Lista inicial de classificação dos participantes
classificacao = ['Ana', 'Carlos', 'Pedro']

# Exibe a lista atual de classificação
print(f"Lista atual: {classificacao}")

# Solicita o nome incorreto
nome_incorreto = input("Digite o nome incorreto: ").strip()

# Solicita o nome correto
nome_correto = input("Digite o nome correto: ").strip()

# Verifica se o nome incorreto está na lista
if nome_incorreto in classificacao:
    # Substitui o nome incorreto pelo nome correto
    indice = classificacao.index(nome_incorreto)
    classificacao[indice] = nome_correto
    print(f"O nome {nome_incorreto} foi substituído por {nome_correto}.")
else:
    print(f"O nome {nome_incorreto} não foi encontrado na lista.")

# Exibe a lista atualizada de classificação
print(f"Lista atualizada: {classificacao}")