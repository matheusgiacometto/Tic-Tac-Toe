def main():
    print('Welcome to the Tic Tac Toe by Team 2')

    print('Instruções')

    player1 = input('Please enter your name Player 1: ')
    player2 = input('Please enter your name Player 2: ')

    jogo = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


    for i in range (0,9):
        if (i%2 == 0):
            print(player1+'`s turn')
            m = input('Linha: ')
            n = input('Coluna: ')
            jogo[int(m)][int(n)] = 'x'
            print_table(jogo[0][0],jogo[0][1],jogo[0][2],jogo[1][0],jogo[1][1],jogo[1][2],jogo[2][0],jogo[2][1],jogo[2][2])
            verifica(jogo,player1,player2,i)
        elif (i%2 == 1):
            print(player2 + '`s turn')
            m = input('Linha: ')
            n = input('Coluna: ')
            jogo[int(m)][int(n)] = 'o'
            print_table(jogo[0][0], jogo[0][1], jogo[0][2], jogo[1][0], jogo[1][1], jogo[1][2], jogo[2][0], jogo[2][1],
                        jogo[2][2])
            verifica(jogo,player1,player2,i)
        else:
            return 0




def print_table(a, b, c, d, e, f, g, h, i):
    print(' ' + a + ' | '+ b +' | '+ c +' ')
    print('-----------')
    print(' ' + d + ' | ' + e + ' | ' + f + ' ')
    print('-----------')
    print(' ' + g + ' | ' + h + ' | ' + i + ' ')


def verifica(matriz,player1,player2,i):
    if (matriz[0][0] == 'x' and matriz[0][1] == 'x' and matriz[0][2] == 'x'):
        print(player1+' wins')
        return 0
    elif (matriz[1][0] == 'x' and matriz[1][1] == 'x' and matriz[1][2] == 'x'):
        print(player1+' wins')
        return 0
    elif (matriz[2][0] == 'x' and matriz[2][1] == 'x' and matriz[2][2] == 'x'):
        print(player1+' wins')
        return 0
    elif (matriz[0][0] == 'x' and matriz[1][0] == 'x' and matriz[2][0] == 'x'):
        print(player1+' wins')
        return 0
    elif (matriz[0][1] == 'x' and matriz[1][1] == 'x' and matriz[2][1] == 'x'):
        print(player1+' wins')
        return 0
    elif (matriz[0][2] == 'x' and matriz[1][2] == 'x' and matriz[1][2] == 'x'):
        print(player1+' wins')
        return 0
    elif (matriz[0][0] == 'x' and matriz[1][1] == 'x' and matriz[2][2] == 'x'):
        print(player1+' wins')
        return 0
    elif (matriz[0][2] == 'x' and matriz[1][1] == 'x' and matriz[2][0] == 'x'):
        print(player1+' wins')
        return 0
    else:
        if (i == 9):
            print('We have a draw')
            return 0


    if (matriz[0][0] == 'o' and matriz[0][1] == 'o' and matriz[0][2] == 'o'):
        print(player2+' wins')
        return 0
    elif (matriz[1][0] == 'o' and matriz[1][1] == 'o' and matriz[1][2] == 'o'):
        print(player2+' wins')
        return 0
    elif (matriz[2][0] == 'o' and matriz[2][1] == 'o' and matriz[2][2] == 'o'):
        print(player2+' wins')
        return 0
    elif (matriz[0][0] == 'o' and matriz[1][0] == 'o' and matriz[2][0] == 'o'):
        print(player2+' wins')
        return 0
    elif (matriz[0][1] == 'o' and matriz[1][1] == 'o' and matriz[2][1] == 'o'):
        print(player2+' wins')
        return 0
    elif (matriz[0][2] == 'o' and matriz[1][2] == 'o' and matriz[1][2] == 'o'):
        print(player2+' wins')
        return 0
    elif (matriz[0][0] == 'o' and matriz[1][1] == 'o' and matriz[2][2] == 'o'):
        print(player2+' wins')
        return 0
    elif (matriz[0][2] == 'o' and matriz[1][1] == 'o' and matriz[2][0] == 'o'):
        print(player2+' wins')
        return 0
    else:
        if (i == 9):
            print('We have a draw')
            return 0

main()
