print(r"""
      
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                              
                                              

      """)

# Definindo as operações usando funções lambda
operacoes = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Erro: Divisão por zero"
}

# Solicitar entrada do usuário
primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))
operador = input("Escolha a operação (| + | - | * | / |): ")

# Verificar se o operador é válido e calcular o resultado
if operador in operacoes:
    resultado = operacoes[operador](primeiro_numero, segundo_numero)
    print(f"O resultado é: {resultado}")
else:
    print("Operador inválido. Por favor, escolha entre +, -, * ou /.")