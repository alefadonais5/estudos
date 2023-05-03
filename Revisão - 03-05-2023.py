# Tipos de variaveis - Numericos (Real, Inteiro-Float, Int), String(Caracteres), Boleano (True, Falso)
#Operadores Aritmeticos
#Operadores Lógico - And, or, Not
#Operadores Relacionais -
#Operadores de atribuições (+= atribuir soma, -= atribuir subtrair,
#Decisão - Será cobrado estrutura correta
#Tipos de variaveis
#Repetição(1 Questão de for simples, 1 questão de for com array, 1 questão de while)

Cont = 'S'
M = []


while Cont == "S":
    num1 = float(input("Escreva a primeira nota: "))
    num2 = float(input("Escreva a segunda nota: "))
    media = (num1+num2)/2
    M.append(media)

    if media >= 7.0:
        print("Aluno aprovado com média: ", media)
    elif media >= 4.0:
        print("Aluno em recuperação com média", media)
    else:
        print("Aluno em reprovado", media)

    Cont = input("Deseja continuar? ")
else:
    print(M)
    print("Fim do programa!")

