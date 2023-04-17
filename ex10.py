#Ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive)
numero=int(input("Digite o número: "))
if numero>0:
    for x in range(1,numero+1):
        print(x)
else:
    print("numero inválido")