

print("Digite os 3 lados do triangulo")
lado1 = float (input("Lado 1:"))
lado2 = float (input("Lado 2:"))
lado3 = float (input("Lado 3:"))


if lado1 + lado2 > lado3:
   triangulo = True
else:
    triangulo = False
    
if triangulo == False:
    print("Valores invalidos, um dos lados do triangulo não pode ser maior que os outros 2 somados.")

else:
    if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        print("Triangulo Equilatero.")
        
    elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
        print("Triangulo Isósceles.")
    
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("Triangulo Escaleno.")