
nome = str(input("Digite seu nome: "))
turno = str(input("Qual turno voce estuda ? M - MATUTINO -----  V - VESPERTINO ------- N - NOITE "))

if turno == "M" or turno == "m":
   print("Bom dia, ",nome," !")
    
elif turno == "V" or turno == "v":
    print("Boa tarde, ",nome," !")
    
elif turno == "N" or turno == "n":
    print("Boa noite, ",nome," !")
    
else:
    print("Valor Invalido, digite novamente.")