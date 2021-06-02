import random

def jogar():
    print("*********************************")
    print("*** Bem vindo ao jogo da Forca!*** ")
    print("*********************************")

    arquivo = open("arquivos.txt","r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero]
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0
    print("Dica da palavra", letras_acertadas)
    while(not enforcou and not acertou ):

        chute = input("Qual letra ?")
        chute = chute.strip().upper()
        print("...")
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        print("Voce ganhou !!!")
    else:
        print("Voce perdeu !!!")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
