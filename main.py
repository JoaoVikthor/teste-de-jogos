print("*********************************")
print("*bem vindo ao jogo de advinhaçao*")
print("*********************************")

numero_secreto: int = 42

chute_str = input("Digite o seu numero:")
chute=int(chute_str)
print("VOCE DIGITOU", chute)

acertou = numero_secreto == chute
maior=chute < numero_secreto
menor=chute > numero_secreto

if(acertou):
        print("voce acertou")
else:

    if(maior):
        print("O seu chute foi maior que o numero secreto")
    elif(menor):
            print("O seu chute foi menor que o nuemro secreto")

print("FIM DE JOGO")



