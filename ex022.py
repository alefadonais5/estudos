alunos = []
quant = int(input("Digite quantidade de alunos?"))

for x in range(quant):
    alunos.append(input("Digite o nome do aluno: "))
for i in range(x+1):
    print(alunos[i], i)

nome = input("digite o nome?")
for y in range(x):
    if nome == alunos[y]:
        print(y, alunos[y])