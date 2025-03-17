print(r"""
      
 ___       ___  ________  _________  ________     
|\  \     |\  \|\   ____\|\___   ___\\   __  \    
\ \  \    \ \  \ \  \___|\|___ \  \_\ \  \|\  \   
 \ \  \    \ \  \ \_____  \   \ \  \ \ \   __  \  
  \ \  \____\ \  \|____|\  \   \ \  \ \ \  \ \  \ 
   \ \_______\ \__\____\_\  \   \ \__\ \ \__\ \__\
    \|_______|\|__|\_________\   \|__|  \|__|\|__|
                  \|_________|                    
                                                  
                                                  

      """)


convidados = set() 
  
while True: 
    nome = input("Digite o nome do convidado ou 'sair' para encerrar: ") 

    if nome.lower() == "sair": 
        break 

    convidados.add(nome) 

print(f"Convidados confirmados: {', '.join(convidados)}") 