vetor = []

for i in range(10):
    vetor.append(float(input("Digite o número: ")))

novo_num = (float(input("Digite um novo número: ")))

cont = 0

for x in range(10):
    if vetor[x] == novo_num:
        cont+=1
print(cont)