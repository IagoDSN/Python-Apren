while True:
    print(" ")
    try:
        entrada = int(input("Digite um numero inteiro: "))
        for entrada in range(entrada, 0, -1):
            print("n:",entrada, end=" ")
            d = True
    except:
        print("Digite um número inteiro!")
        d = False

    if d == True:
        break

print("\n", "Feito!")