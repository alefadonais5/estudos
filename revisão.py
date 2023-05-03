#Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos,
#nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

Eleitores = int(input("Qual a quantidade de eleitores? "))
Votos_Brancos = int(input("Qual a quantidade de votos brancos? "))
Votos_Nulos = int(input("Qual a quantidade de votos nulos? "))
Votos_Validos = int(input("Quantos votos válidos? "))

Percentual_Brancos = (Votos_Brancos*Eleitores)/100
Percentual_Nulos = (Votos_Nulos*Eleitores)/100
Percentual_Validos = (Votos_Validos*Eleitores)/100

print("Total de eleitores: ", Eleitores, "Votos Brancos", Percentual_Brancos,"%, Votos Nulos", Percentual_Validos, "Votos válidos", Percentual_Validos,"%")