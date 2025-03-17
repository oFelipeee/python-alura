print(r"""
      
 __    __   ______  ________   ______    ______            
|  \  |  \ /      \|        \ /      \  /      \           
| $$\ | $$|  $$$$$$\\$$$$$$$$|  $$$$$$\|  $$$$$$\       __ 
| $$$\| $$| $$  | $$  | $$   | $$__| $$| $$___\$$      |  \
| $$$$\ $$| $$  | $$  | $$   | $$    $$ \$$    \        \$$
| $$\$$ $$| $$  | $$  | $$   | $$$$$$$$ _\$$$$$$\       __ 
| $$ \$$$$| $$__/ $$  | $$   | $$  | $$|  \__| $$      |  \
| $$  \$$$ \$$    $$  | $$   | $$  | $$ \$$    $$       \$$
 \$$   \$$  \$$$$$$    \$$    \$$   \$$  \$$$$$$           
                                                           
                                                           
                                                           

      """)

# Solicita as notas dos alunos
notas_input = input("Digite as notas dos alunos separadas por vírgula: ")

# Converte a string de notas em uma lista de floats
notas = [float(nota.strip()) for nota in notas_input.split(',')]

# Calcula a média das notas
if notas:  # Verifica se a lista não está vazia
    media = sum(notas) / len(notas)
    # Exibe a média final da turma com duas casas decimais
    print(f"Média final da turma: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")