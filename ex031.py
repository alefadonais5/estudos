#exercicio 13 do slides 13
a = []
for i in range(5):
    a.append(int(input("Digite o número :")))

for y in range(5):
    if a[y] % 2 == 0:
        print(a[y])

soma = 0
for r in range(5):
    soma = soma+a[r]

media = soma/5
print("Média: ", media)

Numero_Maior = a[0]
for p in range(5):
    if a[p] > Numero_Maior:
        Numero_Maior = a[p]

Numero_Menor = a[0]
for t in range(5):
    if a[t] > Numero_Menor:
        Numero_Menor = a[t]


print(Numero_Maior)
print(Numero_Menor)

cont = 0

for o in range(5):
    if a[o] > media:
        cont += 1
print("A quantidade de números maior que a média é: ", cont)
