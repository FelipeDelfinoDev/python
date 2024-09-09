import random
import cowsay #biblioteca para desenhos
resp = 'S'

while resp == 'S':
    cpu = random.randint(1,100)
    print('-' * 50)
    print('                jogo da adivinhação       ')
    print('-' * 50)

    print('escolha uma dificuldade: \n')

    while True:    #controla dificuldade do jogo
        level = int(input('[1] facil: 12 vidas \n[2] medio 10 vidas \n[3] dificil 7 vidas \n'))
        if level == 1:
            cont = 12
            break

        elif level == 2:
            cont = 10
            break

        elif level == 3:
            cont = 7
            break

        else:
            print('Codigo Invalido! \n tente novamente')

    cowsay.tux('tente adivinhar o numero que estou pensando ')
    while True: 
        (f'numero de vidas: {cont}') #contador de chances da rodada
        player = int(input('digite um numero: '))
        cont = cont - 1 #numero de vidas
        if player < cpu: 
            cowsay.tux(f'o numero é maior que {player} ') #if o jogador digitar um numero menor que o numero pensado pela cpu

        elif player > cpu:
            cowsay.tux(f'o numero é menor que: {player} ') #if o jogador um numero maior que o numero pensado pela cpu

        elif player == cpu:
            cowsay.tux(f' PARABENS!! Voce acertou o numero ') #if o jogador acertar o numero
            break          #quebra o laço de repetição 

        if cont == 0:
            cowsay.tux(f'Voce Perdeu! o numero era {cpu} ') #if o jogador não acertar o numero e as vidas chegarem a zero
            break  

        print(f'numero de vidas: {cont} ') #contador de chances apos erro

    resp = input('digite S para continuar jogando qualquer outra letra para sair: ').upper() #controla o laço 

print('jogo encerrado, obrigado por jogar <3')