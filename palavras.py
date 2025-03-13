# Solicita ao usuário que digite o texto a ser revisado
texto = input("Digite o texto a ser revisado: ")

# Solicita a palavra que será substituída
palavra_substituir = input("Qual palavra deseja substituir? ")

# Solicita a nova palavra
nova_palavra = input("Qual a nova palavra? ")

# Substitui todas as ocorrências da palavra no texto
texto_revisado = texto.replace(palavra_substituir, nova_palavra)

# Exibe o texto com as alterações aplicadas
print(texto_revisado)