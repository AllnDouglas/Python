num1 = int(input("Digite um numero: "))

if num1 < 0:
    print(num1,"é negativo.")
elif num1 > 0:
    print(num1,"é positivo.")
else:
    if num1 == 0:
        print(num1,"é um numero neutro")