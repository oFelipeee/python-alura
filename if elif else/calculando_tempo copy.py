A = int(input('Informe os dias para a atividade A: '))
B = int(input('Informe os dias para a atividade B: '))
C = int(input('Informe os dias para a atividade C: '))

if A > 0 and B > 0 and C > 0:
    soma = A + B + C
    print(f'Tempo total do projeto: {soma} dias')
else:
    print('valor negativo encontrado. Insira apenas os números positivos.')