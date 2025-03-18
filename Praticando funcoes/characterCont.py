print(r"""
      
                 _            _            
                | |          | |           
  ___ ___  _ __ | |_ __ _  __| | ___  _ __ 
 / __/ _ \| '_ \| __/ _` |/ _` |/ _ \| '__|
| (_| (_) | | | | || (_| | (_| | (_) | |   
 \___\___/|_| |_|\__\__,_|\__,_|\___/|_|   
                                           
                                           

      """)

def contar_caracteres(palavra):
    quantidade = len(palavra)
    return quantidade

# Solicitar entrada do usuário
palavra = input("Digite uma palavra: ")

# Contar os caracteres
quantidade_caracteres = contar_caracteres(palavra)

# Exibir o resultado
print(f"Essa palavra tem {quantidade_caracteres} caracteres.")