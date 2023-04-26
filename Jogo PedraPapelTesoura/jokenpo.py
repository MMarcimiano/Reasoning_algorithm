#Trabalho Mateus Marcimiano Jokenpo
from random import randint

placar_P1 = 0
placar_P2 = 0
placar_comp = 0
placar_player = 0
while True:
    modo = int(input('Você quer jogar no modo PvP (1) ou PvE (2)? Para encerrar digite (0): '))
    print('')
    if modo == 0:
        print('Jogo encerrado!')
        break

    if modo == 1:
        while True:
            print('(1) Pedra')
            print('(2) Papel')
            print('(3) Tesoura')
            print('(0) Para voltar ao menu')
            p1 = int(input('Player1, digite o número correspondente a sua escolha:'))
            p2 = int(input('Player2, digite o número correspondente a sua escolha:'))
            
            if p1 == p2 and p1 != 0 and p2 != 0:
                print('Empate!')
                print('Player1', placar_P1, 'x', placar_P2, 'Player2')
                print('')
            elif p1 == 1 and p2 == 2:
                print('Player2 venceu!')
                placar_P2 += 1
                print('Player1', placar_P1, 'x', placar_P2, 'Player2')
                print('')
            elif p1 == 1 and p2 == 3:
                print('Player1 venceu!')
                placar_P1 += 1
                print('Player1', placar_P1, 'x', placar_P2, 'Player2')
                print('')
            elif p1 == 2 and p2 == 1:
                print('Player1 venceu!')
                placar_P1 += 1
                print('Player1', placar_P1, 'x', placar_P2, 'Player2')
                print('')
            elif p1 == 2 and p2 == 3:
                print('Player2 venceu!')
                placar_P2 += 1
                print('Player1', placar_P1, 'x', placar_P2, 'Player2')
                print('')
            elif p1 == 3 and p2 == 1:
                print('Player2 venceu!')
                placar_P2 += 1
                print('Player1', placar_P1, 'x', placar_P2, 'Player2')
                print('')
            elif p1 == 3 and p2 == 2:
                print('Player1 venceu!')
                placar_P1 += 1
                print('Player1', placar_P1, 'x', placar_P2, 'Player2')
                print('')
            elif p1 == 0 or p2 == 0:
                print('Jogo encerrado!')
                print('Player1', placar_P1, 'x', placar_P2, 'Player2')
                print('')
                break

    if modo == 2:
        while True:
            print('(1) Pedra')
            print('(2) Papel')
            print('(3) Tesoura')
            print('(0) Para voltar ao menu')

            p1 = int(input('Player1, digite o número correspondente a sua escolha:'))
            comp = randint(1,3)

            if p1 == comp:
                print('Computador jogou', comp)
                print('Empate!')
                print('Player', placar_player, 'x', placar_comp, 'Computador')
                print('')
            elif p1 == 1 and comp == 2:
                print('Computador jogou', comp)
                print('Computador venceu!')
                placar_comp += 1
                print('Player', placar_player, 'x', placar_comp, 'Computador')
                print('')
            elif p1 == 1 and comp == 3:
                print('Computador jogou', comp)
                print('Player1 venceu!')
                placar_player += 1
                print('Player', placar_player, 'x', placar_comp, 'Computador')
                print('')
            elif p1 == 2 and comp == 1:
                print('Computador jogou', comp)
                print('Player1 venceu!')
                placar_player += 1
                print('Player', placar_player, 'x', placar_comp, 'Computador')
                print('')
            elif p1 == 2 and comp == 3:
                print('Computador jogou', comp)
                print('Computador venceu!')
                placar_comp += 1
                print('Player', placar_player, 'x', placar_comp, 'Computador')
                print('')
            elif p1 == 3 and comp == 1:
                print('Computador jogou', comp)
                print('Computador venceu!')
                placar_comp += 1
                print('Player', placar_player, 'x', placar_comp, 'Computador')
                print('')
            elif p1 == 3 and comp == 2:
                print('Computador jogou', comp)
                print('Player1 venceu!')
                placar_player += 1
                print('Player', placar_player, 'x', placar_comp, 'Computador')
                print('')
            elif p1 == 0:
                print('Jogo encerrado!')
                print('Player', placar_player, 'x', placar_comp, 'Computador')
                print('')
                break