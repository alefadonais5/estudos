div = 0
n1 = float(input("Digite o primeiro número"))
n2 = float(input("Digite o segundo número"))

while n2 == 0:
     print("só permitimos n2 diferentes de ZERO, digite novamente o segundo número")
     n2=float(input())
else:
     div = n1/n2
     print(div)
