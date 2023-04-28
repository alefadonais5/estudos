'''u = []
s = []
for e in range(5):
    u.append(input("Digite o usuário:"))
    s.append(input("Digite sua senha: "))
for i in range(5):
    print("usuario",u[i],s[i], i)'''

u = []
s = []
for e in range(5):
    u.append(input("usuário:"))
    s.append(input("senha: "))

nome = input("Digite seu usuário:")
senha = input("Digite sua senha: ")

cont = 0
for i in range(5):
    if nome == u[i] and senha == s[i]:
        print("Login efetuado com sucesso.")
        break
    else:
        cont+=1

if cont ==5:     #ou nome != u[i] and senha != s[i]:
    print("Não encontrado")

