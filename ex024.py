notas_alunos = []
cont = 0

for x in range(5):
    notas_alunos.append(float(input("Qual a nota do aluno? ")))
soma = 0
for y in range(5):
    soma = soma+notas_alunos[y]
'print(soma)'
media = soma/5


for i in range(5):
    if notas_alunos[i] >= media:
        cont+=1
print(media)
print(cont)




