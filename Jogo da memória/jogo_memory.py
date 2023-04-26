from random import randint
from time import sleep

def gerar_matriz(dificuldade):
    valores = [
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
        ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z', 'AA', 'BB', 'CC', 'DD', 'EE', 'FF'],
        ['GG', 'HH', 'II', 'JJ', 'KK', 'LL', 'MM', 'NN',
        'OO', 'PP', 'QQ', 'RR', 'SS', 'TT', 'UU', 'VV',
        'WW', 'XX', 'YY', 'ZZ', 'AAA', 'BBB', 'CCC', 'DDD',
        'EEE', 'FFF', 'GGG', 'HHH', 'III', 'JJJ', 'KKK', 'LLL', ],
    ]

    matriz = []

    def sortear_cartas():
        matriz_temp = []
        if dificuldade == 1:
            carta = valores[0][randint(0, len(valores[0]) - 1)]
        elif dificuldade == 2:
            matrix_temp = valores[0] + valores[1]
            carta = matrix_temp[randint(0, len(matrix_temp) - 1)]
        else:
            matrix_temp = valores[0] + valores[1] + valores[2]
            carta = matrix_temp[randint(0, len(matrix_temp) - 1)]
        return carta

    def carta_repetida(carta):
        contador = 0
        for linha in range(len(matriz)):
            for coluna in range(len(matriz[linha])):
                if carta == matriz[linha][coluna]:
                    contador += 1
        return contador

    def gerador(nivel):
        for linha in range(nivel):
            matriz.append([])
            for coluna in range(nivel):
                while True:
                    carta = sortear_cartas()
                    if carta_repetida(carta) < 2:
                        matriz[linha].append(carta)
                        break

    if dificuldade == 1:
        nivel = 4

    elif dificuldade == 2:
        nivel = 8
    
    else:
        nivel = 10

    gerador(nivel)
    return matriz

def formatar_mat(mat):
    print()
    for linha in range(len(mat)):
        for coluna in range(len(mat)):
            print(f'[{mat[linha][coluna]:^7}]', end='')
            print()
        
def selecionar_carta():
    linha = int(input('Selecione uma linha: '))
    coluna = int(input('Selecione uma coluna: '))
    return linha - 1, coluna - 1

contador_ajuda = 2
matriz_escondida = []

print('JOGO DA MEMÓRIA')

dificuldade = int(input('[1] Fácil 4x4\n[2] Médio 8x8\n[3] Difícil 10x10\nSelecione a dificuldade: '))
matriz = gerar_matriz(dificuldade)

# Gera a matriz para exibição
for linha in range(len(matriz)):
    matriz_escondida.append([])
    for coluna in range(len(matriz[linha])):
        matriz_escondida[linha].append('#')

while True:

    venceu = False
    formatar_mat(matriz_escondida)

    # print(matriz) # exibir resposta para teste
    print(f'\n[Ajudas restantes = {contador_ajuda}]')
    menu = int(input(('\n[0] Desistir\n[1] Escolher cartas\n[2] Ajuda (mostrar resposta por 3 segundos)\nSelecione uma opção: ')))
    print()

    if menu == 1:
        while True:

            carta_01_linha, carta_01_coluna = selecionar_carta()
            carta_02_linha, carta_02_coluna = selecionar_carta()

            if carta_01_linha == carta_02_linha and carta_01_coluna == carta_02_coluna:
                # Verificar se o usuário escolheu uma carta já selecionada
                print('\nVocê não pode selecionar a mesma carta!')

                formatar_mat(matriz_escondida)
                print(f'\n[Ajudas restantes = {contador_ajuda}]')
                pass

            elif matriz[carta_01_linha][carta_01_coluna] == matriz[carta_02_linha][carta_02_coluna]:
                print('\nACERTOU')

                matriz_escondida[carta_01_linha][carta_01_coluna] = matriz[carta_01_linha][carta_01_coluna]
                matriz_escondida[carta_02_linha][carta_02_coluna] = matriz[carta_02_linha][carta_02_coluna]

                break
            else:
                print('\nERROU')
                break
        
    elif menu == 2:
        if contador_ajuda == 0:
            print('\nOpção indisponível! Suas ajudas acabaram.')

        else:
            print('\n' * 50)
            formatar_mat(matriz)
            sleep(3)
            print('\n' * 50)
            contador_ajuda -= 1

    elif menu == 0:
        print('\nDESISTÊNCIA! VOCÊ PERDEU.')
        break

    if matriz_escondida == matriz:
        print('\nPARABÉNS! VOCÊ VENCEU.')
        venceu = True
        break
       
    if venceu:
        break