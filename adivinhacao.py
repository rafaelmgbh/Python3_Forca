import random
def jogar():
    print("**********************************************")
    print("  Advinhação do numero")
    print("**********************************************")

    print("Qual nível de dificuldade : ")
    print("[1] Fácil  [2] Médio [3] Dificil")
    nivel = int(input("Define o nivel: "))

    numero_secreto = random.randrange(1,101)
    rodada = 1

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    total_ = total_de_tentativas # adicionado esta variavel para armazenar o total de tentativas
    while(total_de_tentativas > 0):
        # Print trabalhando a interpolação de strings
        print("Tentativa {0} de {1}" .format(rodada,total_))
        chute_str = input("Digite o seu número entre 1 e 100 : ")
        print("Voce digitou  : ", chute_str)
        chute = int(chute_str)
        if(chute < 1 or chute > 100 ):
            print("Você deve digitar um número entre 1 e 100")
            continue

        # Transformando o chute informado em numero inteiro .

        if(numero_secreto==chute):
            print("Voce acertou")
            break
        else:
            if(chute>numero_secreto):
                print("Voce errou !!! , seu chute foi maior do que o número secreto")
            if(chute<numero_secreto):
                print("Voce errou !!! ,  seu chute foi menor do que o número secreto")
        total_de_tentativas = total_de_tentativas - 1
        rodada = rodada +1
    print("Fim de jogo")