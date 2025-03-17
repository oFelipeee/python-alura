print(r"""
      
 ______   ______     __    __     __     ______     ______     ______     ______    
/\  == \ /\  ___\   /\ "-./  \   /\ \   /\  ___\   /\  ___\   /\  __ \   /\  __ \   
\ \  _-/ \ \  __\   \ \ \-./\ \  \ \ \  \ \___  \  \ \___  \  \ \  __ \  \ \ \/\ \  
 \ \_\    \ \_____\  \ \_\ \ \_\  \ \_\  \/\_____\  \/\_____\  \ \_\ \_\  \ \_____\ 
  \/_/     \/_____/   \/_/  \/_/   \/_/   \/_____/   \/_____/   \/_/\/_/   \/_____/ 
                                                                                    

      """)

def verificar_permissoes(permissoes_principais, permissoes_solicitadas):
    set_principais = set(permissoes_principais)
    set_solicitadas = set(permissoes_solicitadas)
    
    if set_solicitadas.issubset(set_principais):
        return True
    else:
        return False

def executar_casos():
    casos = [
        (["leitura", "escrita", "execução", "compartilhamento"], ["leitura", "escrita"]),
        (["leitura", "escrita", "execução", "compartilhamento"], ["leitura", "exclusão"])
    ]
    
    for i, (principais, solicitadas) in enumerate(casos, start=1):
        resultado = verificar_permissoes(principais, solicitadas)
        if resultado:
            print(f"Caso {i}: As permissões solicitadas fazem parte das permissões principais.")
        else:
            print(f"Caso {i}: As permissões solicitadas não fazem parte das permissões principais.")

executar_casos()