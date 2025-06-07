print("--------------Lista de nomes---------------")
with open("main.txt", "a") as arquivo:
    arquivo.write("")
while(True):
    d = int(input("\n|1| para registrar um nome\n|2| para ler algum nome\n|3| Para deletar algum nome\n|4| para sair\nDigite aqui: "))
    try:
        match(d):
            case 1:
                try:
                    principal = str(input("Digite o nome: "))
                    with open("main.txt", "a") as arquivo:
                        arquivo.write("\n" + principal)
                except FileNotFoundError:
                    print("O arquivo não foi encontrado, verifique a pasta principal!") 
            case 2:
                try:
                    linhas = []
                    with open("main.txt", "r") as arquivo:
                        for linha in arquivo:
                            linhas.append(linha.strip())
                        for i in linhas:
                            print(i)

                except FileNotFoundError:
                    print("O arquivo não foi encontrado, verifique a pasta principal!")
            case 3:
                try:
                    linhas = []
                    with open("main.txt", "r") as arquivo:
                        for linha in arquivo:
                            linhas.append(linha.strip())
                        for i in linhas:
                            print(i)
                    remover = str(input("Digite qual nome deseja remover: "))
                    with open("main.txt", "w") as arquivo:
                        for linha in linhas:
                            if linha.strip() != remover:
                                arquivo.write(linha)
                            else:
                                arquivo.write("")
                except FileNotFoundError:
                    print("O arquivo não foi encontrado, verifique a pasta principal!")
            case 4:
                break
            case _:
                print("opção invalida, Tente novamente")
    except:
        print("Digite um valor válido!")