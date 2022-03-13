import os
import random

jogarNovamente = 's'
jogadas = 0
quemJoga = 2 #1 = cpu e 2 = jogador
maxJogadas = 9
vit = 'n'
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def tela():
    global velha
    global jogadas
    os.system('cls')
    print("   0   1   2 ")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + ' | ' + velha[0][2])
    print('   -----------')
    print("1:  " + velha[1][0] + " | " + velha[1][1] + ' | ' + velha[1][2])
    print('   -----------')
    print("2:  " + velha[2][0] + " | " + velha[2][1] + ' | ' + velha[2][2])
    print('   -----------')
    print(f'Jogadas: {jogadas}')


def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input('Linha..: '))
            c = int(input('Coluna..: '))
            while velha[l][c] != " ":
                l = int(input('Linha..: '))
                c = int(input('Coluna..: '))
            velha[l][c] = 'X'
            quemJoga = 1
            jogadas += 1
        except:
            print('Jogada inválida!')
            os.system ('pause')


def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = 'O'
        jogadas += 1
        quemJoga = 2


def verificarVitoria():
    global velha
    vioria = 'n'
    simbolos = ["X", "O"]
    for s in simbolos:
        vitoria = 'n'


        #Verificar linhas
        il = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
              if velha[il][ic] == s:
                  soma += 1
              ic += 1
            if soma == 3:
                vitoria = s
                break
            il += 1
        if vitoria != 'n':
            break


        #Verificar Colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if velha[il][ic] == s:
                    soma += 1
                il += 1
            if soma == 3:
                vitoria = s
                break
            ic += 1
        if vitoria != 'n':
            break


        #Verifica diagonal 1
        soma = 0
        indiag = 0
        while indiag < 3:
            if velha[indiag][indiag] == s:
                soma += 1
            indiag += 1
        if soma == 3:
            vitoria = s
            break


        #Verifica diagoal 2:
        soma = 0
        indiagl = 0
        indiagc = 2
        while indiagc >= 0:
            if velha[indiagl][indiagc] == s:
                soma += 1
            indiagl += 1
            indiagc -= 1
        if soma == 3:
            vitoria = s
            break
    return vitoria


def redefinir():
    global velha
    global jogadasglobal
    global quemJoga
    global maxJogadas
    global vit
    jogadas = 0
    quemJoga = 2  # 1 = cpu e 2 = jogador
    maxJogadas = 9
    vit = 'n'
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]


while jogarNovamente == 's':
    while True:
        tela()
        jogadorJoga()
        cpuJoga()
        tela()
        vit = verificarVitoria()
        if vit != 'n' or jogadas >= maxJogadas:
            break

    print('Fim de jogo!')
    if vit == 'X' or vit == 'O':
        print(f'Resultado: Jogador {vit} venceu')
    else:
        print('Resultado: Empate')
    jogarNovamente = input('Jogar novamente? [S/N]: ')
    redefinir()
