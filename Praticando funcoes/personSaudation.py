print(r"""
      
 _          _ _                                           
| |        | | |                                          
| |__   ___| | | ___   ___   ___   ___   ___   ___   ___  
| '_ \ / _ \ | |/ _ \ / _ \ / _ \ / _ \ / _ \ / _ \ / _ \ 
| | | |  __/ | | (_) | (_) | (_) | (_) | (_) | (_) | (_) |
|_| |_|\___|_|_|\___/ \___/ \___/ \___/ \___/ \___/ \___/ 
                                                          
                                                          

      """)

def saudacao_por_hora(hora):
    if hora < 0 or hora > 23:
        return "Hora inválida. Por favor, insira uma hora entre 0 e 23."
    elif hora < 12:
        return "Bom dia!"
    elif 12 <= hora < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

# Solicitar entrada do usuário
hora_atual = int(input("Digite a hora atual (0-23): "))

# Obter a saudação
mensagem = saudacao_por_hora(hora_atual)

# Exibir o resultado
print(mensagem)