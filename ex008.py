#Ler uma variavel de número inteiro e mostrar a tabuada desse número.

num=int(input("Escreva o número:"))
for y in range(11):
    print(y, "*", num, "=", num*y)