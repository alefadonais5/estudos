n = int(input("Digite o tamanho do vetor: "))
A = []
B = []
C = []

for i in range(n):
    A.append(int(input("Digite o primeiro número")))
    B.append(int(input("Digite o segundo número")))

for i in range(n):
    C.append(A[i]+B[i])

print(A,B,C)