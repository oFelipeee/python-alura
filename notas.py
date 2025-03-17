print(r"""
$$\   $$\  $$$$$$\ $$$$$$$$\  $$$$$$\   $$$$$$\  
$$$\  $$ |$$  __$$\\__$$  __|$$  __$$\ $$  __$$\ 
$$$$\ $$ |$$ /  $$ |  $$ |   $$ /  $$ |$$ /  \__|
$$ $$\$$ |$$ |  $$ |  $$ |   $$$$$$$$ |\$$$$$$\  
$$ \$$$$ |$$ |  $$ |  $$ |   $$  __$$ | \____$$\ 
$$ |\$$$ |$$ |  $$ |  $$ |   $$ |  $$ |$$\   $$ |
$$ | \$$ | $$$$$$  |  $$ |   $$ |  $$ |\$$$$$$  |
\__|  \__| \______/   \__|   \__|  \__| \______/ 
                                                 
                                                 
                                                 
      """)

# Função para ordenar as notas
def ordenar_notas(notas):
    return sorted(notas)

# Solicita ao usuário que insira as notas
entrada = input("Digite as notas dos participantes separadas por vírgula: ")

# Converte a entrada em uma lista de inteiros
notas = [int(nota.strip()) for nota in entrada.split(",")]

# Ordena as notas
notas_ordenadas = ordenar_notas(notas)

# Exibe as notas ordenadas
print(f"Notas ordenadas: {notas_ordenadas}")