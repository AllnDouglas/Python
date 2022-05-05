

valor_saque = int (input("Digite o valor que deseja sacar: [10] a [600] ..."))

cem = int(valor_saque / 100)
valor_saque = valor_saque - (cem * 100)
 
cinquenta = int(valor_saque / 50)
valor_saque = valor_saque - (cinquenta * 50)
 
vinte = int(valor_saque /20)
valor_saque = valor_saque - (vinte * 20)
 
dez = int(valor_saque / 10)
valor_saque = valor_saque - (dez * 10)
 
cinco = int(valor_saque / 5)
valor_saque = valor_saque - (cinco * 5)
 
um = valor_saque

print("notas de cem:",cem)
print("notas de cinquenta:",cinquenta)
print("notas de vinte:",vinte)
print("notas de dez:",dez)
print("notas de cinco:",cinco)
print("moedas de um:",um)

 