print(r"""
      
$$$$$$$\  $$\                                                             
$$  __$$\ \__|                                                            
$$ |  $$ |$$\  $$$$$$$\  $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$$\  $$$$$$\  
$$ |  $$ |$$ |$$  _____|$$  __$$\ $$  __$$\ $$  __$$\ $$  _____| \____$$\ 
$$ |  $$ |$$ |\$$$$$$\  $$ /  $$ |$$$$$$$$ |$$ |  $$ |\$$$$$$\   $$$$$$$ |
$$ |  $$ |$$ | \____$$\ $$ |  $$ |$$   ____|$$ |  $$ | \____$$\ $$  __$$ |
$$$$$$$  |$$ |$$$$$$$  |$$$$$$$  |\$$$$$$$\ $$ |  $$ |$$$$$$$  |\$$$$$$$ |
\_______/ \__|\_______/ $$  ____/  \_______|\__|  \__|\_______/  \_______|
                        $$ |                                              
                        $$ |                                              
                        \__|                                              
      """)

# Lista de itens disponíveis na despensa
itens_despensa = ["arroz", "feijão", "açúcar", "sal", "óleo", "macarrão", "café"]

# Solicita ao usuário que digite o item que deseja verificar
item_desejado = input("Digite o item que você quer verificar: ").strip().lower()

# Verifica se o item está na lista de itens disponíveis
if item_desejado in itens_despensa:
    print(f"O item {item_desejado} já está na despensa.")
else:
    print(f"O item {item_desejado} precisa ser comprado.")