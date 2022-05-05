
horas_trabalhadas = int(input("Horas trabalhadas no mês: "))
valor_hora = float(input("Valor hora: "))
salario_bruto = valor_hora * horas_trabalhadas
Imposto_r = int
inss = 10
fgts = 11
d_total = float
salario_liquido = float

if salario_bruto <= 900:
   Imposto_r = 0
   porcentagem_ipr = 0

elif salario_bruto >= 900.01 and salario_bruto <= 1500.00:
     Imposto_r = (5 * salario_bruto) / 100
     porcentagem_ipr = 5

     
elif salario_bruto >= 1500.01 and salario_bruto <= 2500:
     Imposto_r = (10 * salario_bruto) / 100
     porcentagem_ipr = 10
elif salario_bruto > 2500.00:
     Imposto_r = (20 * salario_bruto) / 100
     porcentagem_ipr = 20
     
     
inss = (10 * salario_bruto) / 100
fgts = (11 * salario_bruto) / 100
d_total = inss + fgts + Imposto_r
salario_liquido = salario_bruto - d_total

print("Salario Bruto:",salario_bruto)
print("(-) IR (",porcentagem_ipr,"%)                : R$",Imposto_r)
print("(-) INSS (",10,"%)                           : R$",inss)
print("FGTS (",11,"%)                                : R$",fgts)
print("Total de descontos:                          : R$",d_total)
print("Salario Liquido:                             : R$",salario_liquido)
