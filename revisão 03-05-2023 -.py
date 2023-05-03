#Crie um algoritmo que leia 3 números e diga quem é o maior número.

Num1 = float(input("Digite o primeiro número: "))
Num2 = float(input("Digite o segundo número: "))
Num3 = float(input("Digite o terceiro número: "))

if Num1 > Num2 and Num1 > Num3:
    print("Número maior é ", Num1)
elif Num2 > Num3 and Num2 > Num1:
    print("Número maior é ",Num2)
else:
    print("Número maior é ", Num3)

