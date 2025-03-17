temperatura = input ("Digite a temperatura atual: ")
while temperatura.isalpha() == True:
    temperatura = input ("Valor inválido!. Digite um valor numérico para a temperatura atual: ")
if float(temperatura) > 25:
    print('Alerta!!!!!!!!!!!!!!!! TEMPERATURA ACIMA DO LIMITE PERMITIDO')