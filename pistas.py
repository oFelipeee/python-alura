print(r"""
________                .__  _____                          .___      
\______ \   ____   ____ |__|/ ____\___________    ____    __| _/____  
 |    |  \_/ __ \_/ ___\|  \   __\\_  __ \__  \  /    \  / __ |/  _ \ 
 |    `   \  ___/\  \___|  ||  |   |  | \// __ \|   |  \/ /_/ (  <_> )
/_______  /\___  >\___  >__||__|   |__|  (____  /___|  /\____ |\____/ 
        \/     \/     \/                      \/     \/      \/       
""")

# Função para extrair as três primeiras e as três últimas letras
def extrair_trechos(palavra):
    # Verifica se a palavra tem pelo menos 3 letras
    if len(palavra) < 3:
        return "A palavra deve ter pelo menos 3 letras."
    
    # Extrai as três primeiras e as três últimas letras
    primeiras = palavra[:3]
    ultimas = palavra[-3:]
    
    return primeiras, ultimas

# Solicita ao usuário que digite a palavra-chave
palavra_chave = input("Digite a palavra-chave: ")

# Chama a função para extrair os trechos
primeiras, ultimas = extrair_trechos(palavra_chave)

# Exibe os resultados
print(f"Primeiras: {primeiras}")
print(f"Últimas: {ultimas}")