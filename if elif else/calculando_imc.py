pessoa_weight = float(input("Digite o seu peso em (KG): "))
pessoa_height = float(input("Digite sua altura (m): "))

imc = pessoa_weight / (pessoa_height ** 2)
print(f"Seu IMC é: {imc:2f}")

if imc < 18.5:
    print("Você está abaixo do peso. 😨")
elif imc < 25:
    print("Você está com peso normal. 🙂")
elif imc < 30:
    print("Você está com sobrepeso.😦")
elif imc < 35:
    print("Você está com obesidade grau I. 😨")
elif imc < 40:
    print("Você está com obesidade grau II. 😨")
else:
    print("Você está com obesidade grau III. 😨")