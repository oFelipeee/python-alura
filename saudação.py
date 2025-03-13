# Função para criar a mensagem de boas-vindas
def criar_mensagem_boas_vindas(nome, cidade):
    mensagem = f"Olá, {nome}! Bem-vinda ao sistema da cidade de {cidade}."
    return mensagem

# Solicita ao usuário que digite o nome e a cidade do cliente
nome_cliente = input("Digite o nome do cliente: ")
cidade_cliente = input("Digite a cidade do cliente: ")

# Chama a função para criar a mensagem de boas-vindas
mensagem_boas_vindas = criar_mensagem_boas_vindas(nome_cliente, cidade_cliente)

# Exibe a mensagem
print(mensagem_boas_vindas)