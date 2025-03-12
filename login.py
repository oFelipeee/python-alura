import time

def estilo(texto, cor):
    cor_map = {
        'vermelho': '\033[91m',
        'verde': '\033[92m',
        'amarelo': '\033[93m',
        'reset': '\033[0m'
    }
    return f"{cor_map.get(cor, cor_map['reset'])}{texto}{cor_map['reset']}"

while True:
    nome_usuario = input(estilo("Digite seu nome de usuário: ", "amarelo"))
    senha = input(estilo("Digite sua senha: ", "amarelo"))

    if len(nome_usuario) < 5:
        print(estilo("O nome de usuário deve ter pelo menos 5 caracteres.", "vermelho"))
        continue

    if len(senha) < 8:
        print(estilo("A senha deve ter pelo menos 8 caracteres.", "vermelho"))
        continue

    print(estilo("Cadastro realizado com sucesso!", "verde"))
    break

# Contagem regressiva
for i in range(10, 0, -1):
    if i > 1:
        print(estilo(f"Faltam apenas {i} segundos - Não perca essa oportunidade!", "amarelo"))
        print(estilo(f"A contagem continua: {i-1} segundos restantes.", "amarelo"))
    else:
        print(estilo("Aproveite a promoção agora!", "verde"))
    time.sleep(1)