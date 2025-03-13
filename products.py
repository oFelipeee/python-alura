# Função para padronizar o nome do produto
def padronizar_nome_produto(nome):
    # Remove espaços no início e no final e converte para minúsculas
    nome_padronizado = nome.strip().lower()
    return nome_padronizado

# Solicita ao usuário que digite o nome do produto
nome_produto = input("Digite o nome do produto: ")

# Chama a função para padronizar o nome do produto
nome_padronizado = padronizar_nome_produto(nome_produto)

# Exibe o resultado
print(nome_padronizado)