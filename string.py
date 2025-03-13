print(r"""
  _________ __         .__                
 /   _____//  |________|__| ____    ____  
 \_____  \\   __\_  __ \  |/    \  / ___\ 
 /        \|  |  |  | \/  |   |  \/ /_/  >
/_______  /|__|  |__|  |__|___|  /\___  / 
        \/                     \//_____/  
"""
      )

url = input("Digite a URL para validação: ") 
if url.startswith("https://") and url.endswith(".com"):
    print("URL válida!")
else:
    print("URL inválida!")