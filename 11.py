#receba um número, do usuário e diga se ele é par ou ímpar

#Esse código é mais limpo.

numero = int(input("Escreva o número"))

if numero==0:
    print("Número inválido")
else:
    if numero%2:
        print("Esse número é impar")
    else:
        print("Esse número é par")