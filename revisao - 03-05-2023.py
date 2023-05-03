#Escreva um número diferente de zero e diga se é positovo ou negativo

"""Cont = "S"
while Cont == "S":
    num1 = float(input("Digite o número: "))
    if num1 < 0:
        print("Número negativo", num1)
    elif num1 > 0:
        print("Número posito", num1)
    else:
        print("Número não pode ser igual a zero.")

    Cont = input("Tem um novo número? S/N ")
else:
    print("Programa encerrado.")"""

#OUTRA FORMA DE FAZER ESSA QUESTÃO.
Resp = "S"
while Resp == "S":
    num = int(input("Digite o número: "))

    if num != 0:
        if num > 0:
            print("Número posito")
        else:
            print("Número negativo")
    else:
        print("Número é igual a zero. só aceitamos números de diferente de 0")
    Resp = input("Deseja continuar? S/N")

        