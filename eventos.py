print(r"""
      
 ________                                 __                         
|        \                               |  \                        
| $$$$$$$$__     __   ______   _______  _| $$_     ______    _______ 
| $$__   |  \   /  \ /      \ |       \|   $$ \   /      \  /       \
| $$  \   \$$\ /  $$|  $$$$$$\| $$$$$$$\\$$$$$$  |  $$$$$$\|  $$$$$$$
| $$$$$    \$$\  $$ | $$    $$| $$  | $$ | $$ __ | $$  | $$ \$$    \ 
| $$_____   \$$ $$  | $$$$$$$$| $$  | $$ | $$|  \| $$__/ $$ _\$$$$$$\
| $$     \   \$$$    \$$     \| $$  | $$  \$$  $$ \$$    $$|       $$
 \$$$$$$$$    \$      \$$$$$$$ \$$   \$$   \$$$$   \$$$$$$  \$$$$$$$ 
                                                                     
                                                                     
                                                                     

      """)

# Lista inicial de eventos registrados
eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']

# Exibe a lista de eventos registrados
print(f"Eventos registrados: {eventos_registrados}")

# Corrige a ordem dos eventos invertendo a lista
ordem_corrigida = eventos_registrados[::-1]

# Exibe a ordem corrigida
print(f"Ordem corrigida: {ordem_corrigida}")