
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))


if num1 >= num2 and num1 >= num3 and num2 >= num3:
    print("maior numero: ",num1)
    print("numero do meio: ",num2)
    print("menor numero: ",num3)
    
elif num1 >= num2 and num1 >= num3 and num3 >= num2:
    print("maior numero: ",num1)
    print("numero do meio: ",num3)
    print("menor numero: ",num2)
    
elif num2 >= num1 and num2 >= num3 and num1 >= num3:
     print("maior numero: ",num2)
     print("numero do meio: ",num1)
     print("menor numero: ",num3)
     
elif num2 >= num1 and num2 >= num3 and num3 >= num1:
     print("maior numero: ",num2)
     print("numero do meio: ",num3)
     print("menor numero: ",num1)
     
else: 
    if num3 >= num1 and num3 >= num2 and num1 >= num2:
        print("maior numero: ",num3)
        print("numero do meio: ",num1)
        print("menor numero: ",num2)
    elif num3 >= num1 and num3 >= num2 and num2 >= num1:
        print("maior numero: ",num3)
        print("numero do meio: ",num2)
        print("menor numero: ",num1)
    

