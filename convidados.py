print(r"""
       __        ______   ______  ________   ______  
|  \      |      \ /      \|        \ /      \ 
| $$       \$$$$$$|  $$$$$$\\$$$$$$$$|  $$$$$$\
| $$        | $$  | $$___\$$  | $$   | $$__| $$
| $$        | $$   \$$    \   | $$   | $$    $$
| $$        | $$   _\$$$$$$\  | $$   | $$$$$$$$
| $$_____  _| $$_ |  \__| $$  | $$   | $$  | $$
| $$     \|   $$ \ \$$    $$  | $$   | $$  | $$
 \$$$$$$$$ \$$$$$$  \$$$$$$    \$$    \$$   \$$
                                               
                                               
                                               
      """)


# Lista inicial de convidados
convidados = ['Ana', 'Pedro', 'Carlos']

# Exibe a lista atual de convidados
print(f"Lista atual de convidados: {convidados}")

# Solicita o nome do novo convidado
novo_convidado = input("Digite o nome do novo convidado: ")

# Solicita a posição onde o convidado deve ser inserido
# A posição deve ser um número inteiro
posicao = int(input("Digite a posição na qual deseja inserir o convidado: "))

# Verifica se a posição é válida
if 0 <= posicao <= len(convidados):
    # Insere o novo convidado na posição especificada
    convidados.insert(posicao, novo_convidado)
else:
    print("Posição inválida. A posição deve estar entre 0 e", len(convidados))

# Exibe a lista atualizada de convidados
print(f"Lista atualizada de convidados: {convidados}")