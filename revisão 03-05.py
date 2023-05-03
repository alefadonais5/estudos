#Faça um algoritmo que receba um número inteiro e mostre o seu antecessor.

num = int(input("Digite o número: "))

if num > 0:
    Ant = num -1
    print("O antecessor", Ant)
else:
    Ant = num + 1
    print("O antecessor", Ant)
