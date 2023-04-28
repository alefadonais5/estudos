nomes = []

for y in range(5):
    nomes.append(input("Digite o nome: "))

print(nomes)

for i in range(4,-1,-1):
    print(nomes[i], end="  ")