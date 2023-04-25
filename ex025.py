a = []
m = []

for t in range(10):
    a.append(float(input("Qual o número?")))
x = float(input("Digite o número multiplicador"))


for y in range(10):
    m.append(a[y]*x)

print(a)
print(x)
print(m)