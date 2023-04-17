qtd=int(input("Qual a quantidade de alunos da turma: "))
x=1
soma=0
while x<=qtd:
    num = float(input("Informe a nota: "))
    soma = soma + num #soma+=num (essa soma está escrito da mesma maneira)
    x = x + 1 #x+=1 (escrito da mesma maneira)
media = soma / qtd
print("A média é: ", media)
