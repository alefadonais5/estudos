alunos = []
quant = int(input("Digite quantidade de alunos?"))

for x in range(quant):
    alunos.append(input("Digite o nome do aluno: "))
for i in range(x+1):
    print(alunos[i], i)

nome = input("digite o nome?")
cont = 0
for y in range(x):
    if nome == alunos[y]:
        print(y, alunos[y])
    else:
        cont+=1

if cont == quant:
    print("Não encontrado")