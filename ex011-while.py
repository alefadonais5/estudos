#Ler 10 valores, calcular escrever a média aritmética desses valores lidos(usando While)
x=1
soma=0
while x<=10:
    num=float(input("Informe o número: "))
    soma=soma+num
    x=x+1
media=soma/10
print("A média é: ", media)


