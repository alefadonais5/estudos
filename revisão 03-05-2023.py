#Crie um algoritmo que leia a idade de uma pessoa e diga qual ano nasceu

"""Idade = int(input("Digite sua idade: "))
Ano = 2023-Idade
print("O ano que naceu foi ", Ano)"""

# Crie um algoritmo que leia um número e diga se ele é par ou ímpar.

num = float(input("Escreva o número: "))
if num % 2 == 0:
    if num > 0:
        print("Número par e positivo")
    else:
        print("Número par e negativo")

else:
    if num > 0:
        print("Número é ímpar e positivo")
    else:
        print("Número é ímpar e negativo")
