print(r"""
      
                                              
                                              
  ___ ___  _ ____   _____ _ __ ___  ___  _ __ 
 / __/ _ \| '_ \ \ / / _ \ '__/ __|/ _ \| '__|
| (_| (_) | | | \ V /  __/ |  \__ \ (_) | |   
 \___\___/|_| |_|\_/ \___|_|  |___/\___/|_|   
                                              
                                              

      """)

def converter_telefones(telefones):
    # Converte a lista de strings para inteiros
    return [int(telefone) for telefone in telefones]

def verificar_conversao(telefones_convertidos):
    # Verifica se todos os elementos da lista são inteiros
    return all(isinstance(telefone, int) for telefone in telefones_convertidos)

# Lista de números de telefone armazenados como strings
telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]

# Converter os números de telefone
telefones_convertidos = converter_telefones(telefones)

# Verificar se a conversão foi feita corretamente
if verificar_conversao(telefones_convertidos):
    print("Todos os números foram convertidos corretamente!")
else:
    print("Houve um erro na conversão dos números.")