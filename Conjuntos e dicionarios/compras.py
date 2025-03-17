print(r"""
      
 __         __     ______     ______   ______        _____     ______        ______     ______     __    __     ______   ______     ______     ______    
/\ \       /\ \   /\  ___\   /\__  _\ /\  __ \      /\  __-.  /\  ___\      /\  ___\   /\  __ \   /\ "-./  \   /\  == \ /\  == \   /\  __ \   /\  ___\   
\ \ \____  \ \ \  \ \___  \  \/_/\ \/ \ \  __ \     \ \ \/\ \ \ \  __\      \ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \  _-/ \ \  __<   \ \  __ \  \ \___  \  
 \ \_____\  \ \_\  \/\_____\    \ \_\  \ \_\ \_\     \ \____-  \ \_____\     \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_\    \ \_\ \_\  \ \_\ \_\  \/\_____\ 
  \/_____/   \/_/   \/_____/     \/_/   \/_/\/_/      \/____/   \/_____/      \/_____/   \/_____/   \/_/  \/_/   \/_/     \/_/ /_/   \/_/\/_/   \/_____/ 
                                                                                                                                                         

      """)

def comparar_listas(lista_laura, lista_ana):
    # Converter as listas em conjuntos
    set_laura = set(lista_laura)
    set_ana = set(lista_ana)
    
    # Itens em ambas as listas
    itens_comuns = set_laura.intersection(set_ana)
    
    # Itens exclusivos de Laura
    itens_exclusivos_laura = set_laura.difference(set_ana)
    
    # Itens exclusivos de Ana
    itens_exclusivos_ana = set_ana.difference(set_laura)
    
    return itens_comuns, itens_exclusivos_laura, itens_exclusivos_ana

# Solicitar as listas de compras
lista_laura = input("Lista de Laura (separe os itens por vírgula): ").lower().split(", ")
lista_ana = input("Lista de Ana (separe os itens por vírgula): ").lower().split(", ")

# Comparar as listas
itens_comuns, itens_exclusivos_laura, itens_exclusivos_ana = comparar_listas(lista_laura, lista_ana)

# Exibir os resultados
print("Itens em ambas as listas:", ", ".join(itens_comuns))
print("Itens exclusivos de Laura:", ", ".join(itens_exclusivos_laura))
print("Itens exclusivos de Ana:", ", ".join(itens_exclusivos_ana))