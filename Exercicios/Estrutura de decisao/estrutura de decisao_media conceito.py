

nota1 = float (input("Digite a nota do primeiro semestre"))
nota2 = float (input("Digite a nota do primeiro semestre"))
media = (nota1 + nota2) / 2 




if media >= 9 and media <= 10:
    conceito = "A"

elif media >= 7.5 and media < 9:
    conceito = "B"

elif media >= 6.0 and media < 7.5:
    conceito = "C"

    
elif media >= 4.0 and media < 6.0:
    conceito = "D"

    
elif media >= 0 and media < 4:
    conceito = "E"


if conceito == "A" or conceito == "B" or conceito == "C":
    situacao = "Aprovado"
else :
    situacao = "Reprovado"


print("Nota do primeiro semestre:",nota1)
print("Nota do primeiro semestre:",nota2)
print("Média de aproveitamento:",media)
print("Conceito:",conceito)
print("Situação:",situacao)