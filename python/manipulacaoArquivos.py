try:
    with open("python/teste.txt","a") as arquivo:
        arquivo.write("\nBonJu123")
except FileNotFoundError:
    print("O arquivo não foi encontrado verifique o caminho!")

'''
try:
   with open("python/teste.txt","r") as arquivo:
        conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("O arquivo não foi encontrado verifique o caminho!")
'''

'''
try:
    with open("python/teste.txt", "r") as arquivo:
        for linha in arquivo:
            print(linha.strip())
except FileNotFoundError:
    print("O arquivo não foi encontrado verifique o caminho!")
'''

linhas = []
with open("python/teste.txt", "r") as arquivo:
    for linha in arquivo:
        linhas.append(linha.strip())
print(linhas)

for i in linhas:
    print(i)