import random

print ("********************************")
print ('Bem vindo ao jogo de adivinhação')
print ("********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000

print("Qual o nível de dificuldade", numero_secreto)
print("(1) fácil (2) médio (3) difícil")

nivel = int(input("define o nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("digite um numero entre 1 e 100: ")
    chute = int(chute_str)
   
    if(chute < 1 or chute > 100):
        print("voce deve digitar um numero entre 1 e 100!")
        continue
   
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
   
    if(acertou):
            print("voce acertou e fez {} pontos!" .format(pontos))
            break
    else:
        if(maior):
            print("voce errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("voce errou! O seu chute foi menor do que o número secreto.")
    pontos_perdidos = abs(numero_secreto - chute)  
    pontos = pontos - pontos_perdidos
       
       
print("fim de jogo")
