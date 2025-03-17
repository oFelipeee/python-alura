valores = [10, 20, 30, 40, 50]

def calcular_soma(valores):
    total = sum(valores)
    return total

soma_total = calcular_soma(valores)

print("======================================================")
print("           Relatório de Receitas da Loja             ")
print("======================================================")
print(f"Soma total das receitas: R$ {soma_total}")
print("======================================================")