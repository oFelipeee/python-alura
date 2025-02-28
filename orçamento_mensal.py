limite = 3000.0

al = float(input("alimentação R$ "))
en = float(input("energia R$ "))
ag = float(input("água R$ "))
net = float(input("internet R$ "))
lz = float(input("lazer R$ "))
edc = float(input("educação R$ "))

calc = al + en + ag + net + lz + edc
calc_arredondado = round(calc, 2)

print(f"Seu gasto atual é: R$ {calc_arredondado}")

if calc_arredondado <= limite:
    print("Seus gastos estão dentro do planejado")
else:
    print("Atenção! Você ultrapassou o limite do orçamento.")