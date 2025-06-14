aluc = {"Iago": [10, 7, 8], "Alice": [5, 3, 7], "Joao": [7, 8, 6]}

soma = 0

for aluno, nota in aluc.items():
    for notas in nota:
        soma += notas

media = soma/3

dic = {"Alunos": aluc, "media": media}

print(dic.get("Alunos"), dic.get("media"))