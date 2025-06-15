matriz = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]]

vez = "X"
para = True
vezX = True
vezO = False
vertefica = True
timing = 0

def imprimir():
    print("0",matriz[0][0],"|",matriz[0][1],"|",matriz[0][2])
    print(" -----------")
    print("1",matriz[1][0],"|",matriz[1][1],"|",matriz[1][2])
    print(" -----------")
    print("2",matriz[2][0],"|",matriz[2][1],"|",matriz[2][2])
    print("  0   1   2")

def entrar(entrada1, entrada2):
    global vertefica
    vertefica = True
    if matriz[entrada1][entrada2] == " ":
        if entrada1 >= 0 and entrada1 <=2:
            if entrada2 >= 0 and entrada2 <=2:
                matriz[entrada1][entrada2] = vez
            else:
                print("O segundo número digitado não está disponivel! Tente novamente...")
        else:
            print("O primeiro número digitado não está disponivel! Tente novamente...")
    else:
        vertefica = False

def verifica():
    global para, timing
    if matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X" or matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X" or matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X" or matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X" or matriz[0][2] == "X" and matriz[1][1] == "X" and matriz[2][0] == "X" or matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X" or matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X" or matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X":
        print("O jogador X ganhou!")
        para = False
    else:
        if matriz[0][0] == "O" and matriz[0][1] == "O" and matriz[0][2] == "O" or matriz[1][0] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O" or matriz[2][0] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O" or matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O" or matriz[0][2] == "O" and matriz[1][1] == "O" and matriz[2][0] == "O" or matriz[0][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O" or matriz[0][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O" or matriz[0][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O":
            print("O jogador O ganhou!")
            para = False
        else:
            if timing >= 9:
               print("Empate!")
               para = False 
            else:
                para = True
while True:
    timing = 1
    try:
        print("-----------Jogo da velha-----------")
        quale = int(input("1 - começar\n2 - sair\n:: "))
    except ValueError:
            print("Digite um número inteiro!")
    match(quale):
        case 1:
            imprimir()
            while para:
                vezX = True
                while vezX:
                    try:
                        vez = "X"
                        a, b = map(int, input("(Jogador X)Digite os números da sua posição(coluna linha): ").split())
                        entrar(a,b)
                        if vertefica:
                            imprimir()
                            verifica()
                            timing +=1
                            vezX = False
                        else:
                            print("Este local já está ocupado! Tente novamente...")
                    except ValueError:
                        print("Digite dois números inteiros!")
                if not para:
                    break
                vezO = True
                while vezO:
                    try:
                        vez = "O"
                        a, b = map(int, input("(Jogador O)Digite os números da sua posição(coluna linha): ").split())
                        entrar(a,b)
                        if vertefica:
                            imprimir()
                            verifica()
                            timing +=1
                            vezO = False
                        else:
                            print("Este local já está ocupado! Tente novamente...")
                    except ValueError:
                        print("Digite dois números inteiros!")
        case 2:
            print("-")
            break