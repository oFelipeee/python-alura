time = input("Digite a hora atual (formato 24 horas, exemplo 20:00 ):")
time = time.replace(':',".")
if float(time) < 8 or float(time) > 18 :
    print('Horário de funcionamento das 8:00 às 20:00 hrs, acesso negado')
else:
    print("Acesso Liberado !!!")