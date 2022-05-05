
produto_1 = float(input("Digite o preço do produto: "))
produto_2 = float(input("Digite o preço do segundo produto: "))
produto_3 = float(input("Digite o preço do terceiro produto: "))

# verificando se o produto 1 é menor que o produto 2 e o produto 3
if produto_1 < produto_2 and produto_1 < produto_3:
    print("O primeiro produto tem o melhor preço.")

# verificando se o produto 2 é menor que o produto 1 e o produto 3
elif produto_2 < produto_1 and produto_2 < produto_3:
    print("O segundo produto tem o melhor preço.")


else:
    # verificando se o produto 3 é menor que o produto 1 e o produto 2
    if produto_3 < produto_1 and produto_3 < produto_2:
        print("o terceiro produto tem o menor preço.")
    # verificando se o produto 1 é igual ao produto 2
    elif produto_1 == produto_2:
        print("O primeiro e o segundo produto tem o mesmo preço.")
    else:
        # verificando se o produto 1 é igual ao produto 3
        if produto_1 == produto_3:
            print("O primeiro e o terceiro produto tem o mesmo preço.")
        # verificando se o produto 2 é igual ao produto 3
        elif produto_2 == produto_3:
            print("O segundo e o terceiro produto tem o mesmo preço.")