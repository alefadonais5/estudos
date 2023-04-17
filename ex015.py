cont = "S"
while cont == "S":
    nota1 = float(input("Qual a nota da 1º Avaliação?"))

    while nota1<0 or nota1>10:
        print("O número não pode ser menor que zero ou maior que dez, digite novamente a nota do aluno.")
        nota1 = float(input())

    nota2 = float(input("Qual a nota da 2º Avaliação?"))
    while nota2<0 or nota2>10:
        print("O número não pode ser menor que zero ou maior que dez, digite novamente a nota do aluno.")
        nota2 = float(input())

    media = (nota1+nota2)/2
    print("A média do aluno é ", media)

    cont = input("Deseja continuar? ")
else:
    print("Fim do programa!")


