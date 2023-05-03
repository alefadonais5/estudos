#faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias.
#Considerar ano com 365 dias e mês com 30 dias.

Idade = int(input("Qual a sua Idade? "))
Meses = int(input("Quantos meses? "))
Dias =  int(input("Quantos dias? "))

Total_Dias = (Idade*365) + (Meses*30) + Dias

print("Total de dias: ", Total_Dias)