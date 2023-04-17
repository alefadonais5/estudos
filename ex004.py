#receba um número, do usuário e diga se ele é par ou ímpar

numero = int(input("Escreva o número"))
if numero!=0:
    if numero%2:
        print("Esse número é impar")
    else:
        print("Esse número é par")
else:
    print("Número inválido")

