print(r"""
      
 _______                       __              __                         
|       \                     |  \            |  \                        
| $$$$$$$\  ______    ______   \$$  _______  _| $$_     ______    ______  
| $$__| $$ /      \  /      \ |  \ /       \|   $$ \   /      \  /      \ 
| $$    $$|  $$$$$$\|  $$$$$$\| $$|  $$$$$$$ \$$$$$$  |  $$$$$$\|  $$$$$$\
| $$$$$$$\| $$    $$| $$  | $$| $$ \$$    \   | $$ __ | $$   \$$| $$  | $$
| $$  | $$| $$$$$$$$| $$__| $$| $$ _\$$$$$$\  | $$|  \| $$      | $$__/ $$
| $$  | $$ \$$     \ \$$    $$| $$|       $$   \$$  $$| $$       \$$    $$
 \$$   \$$  \$$$$$$$ _\$$$$$$$ \$$ \$$$$$$$     \$$$$  \$$        \$$$$$$ 
                    |  \__| $$                                            
                     \$$    $$                                            
                      \$$$$$$                                             
""")


# Lista para armazenar os nomes dos voluntários
voluntarios = []

# Loop para registrar os voluntários
while True:
    nome = input("Digite o nome do voluntário (ou 'sair' para encerrar): ").strip()
    
    # Verifica se o usuário deseja sair
    if nome.lower() == 'sair':
        break
    
    # Adiciona o nome à lista de voluntários
    voluntarios.append(nome)

# Exibe a lista completa de voluntários registrados
print(f"Voluntários registrados: {voluntarios}")