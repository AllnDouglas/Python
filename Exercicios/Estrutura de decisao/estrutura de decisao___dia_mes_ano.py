dia = int(input("Digite um dia:"))
mes = int(input("Digite um mes:"))
ano = int(input("Digite um ano:"))

if dia > 32 or dia < 0  or mes < 0 or mes > 12 or ano < 0 or ano > 2022:
    print("Digite uma data valida")
elif ( mes == 2 and dia > 30 ) or (mes == 4 and dia > 30) or (mes == 6 and dia > 30) or (mes == 9 and dia > 30) or (mes == 11 and dia > 31):
    print("Digite uma data valida.")
    
else:
    print("---------- Data ----------")
    print(dia,"/",mes,"/",ano)
    
    