nota_um = float (input("Digite a primeira nota: "))
nota_dois = float (input("Digite a segunda nota: "))
terceira_nota = float (input("Digite a terceira nota: "))
Media = (nota_um + nota_dois + terceira_nota) / 3

if Media >= 7:
    print("Você foi aprovado !!")
elif 5 <= Media < 7:
    print("Recuperação")
else:
    print("Reprovado")