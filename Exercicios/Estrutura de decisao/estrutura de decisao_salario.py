

salario = float(input("Digite seu salario: "))
p_aumento = int
valor_aumento = float

if salario <= 280.00:
   p_aumento = 20
   valor_aumento = (salario * 20) / 100
   
elif salario >= 280.01 and salario <= 700.00:
     p_aumento = 15
     valor_aumento = (salario * 15) / 100
     
elif salario >= 700.01 and salario <= 1500.00:
     p_aumento = 10
     valor_aumento = (salario * 10) / 100
     
elif salario > 1500.00:
    p_aumento = 5
    valor_aumento = (salario * 5) / 100
    

print("Salario antes do reajuste:",salario)
print("Porcentual do aumento: ",p_aumento,"%")
print("Valor do aumento:",valor_aumento)
print("Valor do novo salario:",valor_aumento + salario)
