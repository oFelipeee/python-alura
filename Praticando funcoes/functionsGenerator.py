print(r"""
      
  __                  _   _                          
 / _|                | | (_)                         
| |_ _   _ _ __   ___| |_ _  ___  _ __  ___     __ _ 
|  _| | | | '_ \ / __| __| |/ _ \| '_ \/ __|   / _` |
| | | |_| | | | | (__| |_| | (_) | | | \__ \  | (_| |
|_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/   \__, |
                                                __/ |
                                               |___/ 

      """)

def gerador_desconto(porcentagem_desconto):
    # Closure que calcula o preço final com o desconto
    def calcular_preco_final(valor_compra):
        desconto = valor_compra * (porcentagem_desconto / 100)
        return valor_compra - desconto
    return calcular_preco_final

# Solicitar entrada do usuário
porcentagem_desconto = float(input("Digite a porcentagem de desconto: "))
valor_compra = float(input("Digite o valor da compra: "))

# Gerar a função de cálculo de preço final
calcular = gerador_desconto(porcentagem_desconto)

# Calcular o preço final
preco_final = calcular(valor_compra)

# Exibir o resultado
print(f"Preço final com desconto: {preco_final}")