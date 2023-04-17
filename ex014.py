pin="1010"
senha =input("Digite sua senha: ")
x=0
while senha != pin:
    print("Senha errada. Digite a senha novamente.")
    senha = input()
    x += 1
    if x >= 3 and senha != pin:
        print("Senha bloqueada")
        break

else:
    print("Senha correta!")

