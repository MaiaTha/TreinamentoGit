from random import randint

robozim_w = [
    "Você vai pro RH",
    "Tomou um Update sem where",
]

robozim_l = [
    "Perdi, BANCO DE DADOS!"
]

print("Decida na com Pedra, Papel ou Tesoura quem  vai para o RH, Você ou o RoboZão")
print()
c = int(input("1 para pedra, 2 para papel, 3 para tesoura \n"))


r = randint(1, 3)


print("Robozão: ")
if c == 1:
    if r == 1:
        print("Empate")
    elif r == 2:
        print(robozim_w[1])
    else:
        print(robozim_l[0])
elif c == 2:
    if r == 1:
        print(robozim_l[0])
    elif r == 2:
        print("Empate")
    else:
        print(robozim_w[0])
elif c == 3:
    if r == 1:
        print(robozim_w[1])
    elif r == 3:
        print("Empate")
    else:
        print(robozim_l[0])

