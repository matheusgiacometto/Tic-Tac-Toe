def main():
    print('Welcome to the Tic Tac Toe by Team 2')

    print('Instruções\n')

    player1 = input('Please enter your name Player 1: ')
    player2 = input('Please enter your name Player 2: ')

    jogo = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    i = 0
    while (i < 9):
        if (i % 2 == 0):
            print()
            print(player1 + '`s turn')
            m = input('Linha: ')
            n = input('Coluna: ')
            print()
            if (0 <= int(m) <= 2 and 0 <= int(n) <= 2):
                if (jogo[int(m)][int(n)] == ' '):
                    jogo[int(m)][int(n)] = 'x'
                    print_table(jogo)
                i += 1
            else:
                print('Choose a valid position')


        elif (i % 2 == 1):
            print()
            print(player2 + '`s turn')
            m = input('Linha: ')
            n = input('Coluna: ')
            print()
            if (0 <= int(m) <= 2 and 0 <= int(n) <= 2):
                if (jogo[int(m)][int(n)] == ' '):
                    jogo[int(m)][int(n)] = 'o'
                    print_table(jogo)
                    i += 1
            else:
                print('Choose a valid position')
        else:
            return 0

        result = verify(jogo, player1, player2, i)
        if (result == 1 or result == 2):
            return 0


def print_table(jogo):
    print(' ' + jogo[0][0] + ' | ' + jogo[0][1] + ' | ' + jogo[0][2] + ' ')
    print('-----------')
    print(' ' + jogo[1][0] + ' | ' + jogo[1][1] + ' | ' + jogo[1][2] + ' ')
    print('-----------')
    print(' ' + jogo[2][0] + ' | ' + jogo[2][1] + ' | ' + jogo[2][2] + ' ')


def verify(matriz, player1, player2, i):
    if (matriz[0][0] == 'x' and matriz[0][1] == 'x' and matriz[0][2] == 'x'):
        print(player1 + ' wins')
        return 1
    elif (matriz[1][0] == 'x' and matriz[1][1] == 'x' and matriz[1][2] == 'x'):
        print(player1 + ' wins')
        return 1
    elif (matriz[2][0] == 'x' and matriz[2][1] == 'x' and matriz[2][2] == 'x'):
        print(player1 + ' wins')
        return 1
    elif (matriz[0][0] == 'x' and matriz[1][0] == 'x' and matriz[2][0] == 'x'):
        print(player1 + ' wins')
        return 1
    elif (matriz[0][1] == 'x' and matriz[1][1] == 'x' and matriz[2][1] == 'x'):
        print(player1 + ' wins')
        return 1
    elif (matriz[0][2] == 'x' and matriz[1][2] == 'x' and matriz[1][2] == 'x'):
        print(player1 + ' wins')
        return 1
    elif (matriz[0][0] == 'x' and matriz[1][1] == 'x' and matriz[2][2] == 'x'):
        print(player1 + ' wins')
        return 1
    elif (matriz[0][2] == 'x' and matriz[1][1] == 'x' and matriz[2][0] == 'x'):
        print(player1 + ' wins')
        return 1
    else:
        if (i == 9):
            print('We have a draw')
            return 0

    if (matriz[0][0] == 'o' and matriz[0][1] == 'o' and matriz[0][2] == 'o'):
        print(player2 + ' wins')
        return 2
    elif (matriz[1][0] == 'o' and matriz[1][1] == 'o' and matriz[1][2] == 'o'):
        print(player2 + ' wins')
        return 2
    elif (matriz[2][0] == 'o' and matriz[2][1] == 'o' and matriz[2][2] == 'o'):
        print(player2 + ' wins')
        return 2
    elif (matriz[0][0] == 'o' and matriz[1][0] == 'o' and matriz[2][0] == 'o'):
        print(player2 + ' wins')
        return 2
    elif (matriz[0][1] == 'o' and matriz[1][1] == 'o' and matriz[2][1] == 'o'):
        print(player2 + ' wins')
        return 2
    elif (matriz[0][2] == 'o' and matriz[1][2] == 'o' and matriz[1][2] == 'o'):
        print(player2 + ' wins')
        return 2
    elif (matriz[0][0] == 'o' and matriz[1][1] == 'o' and matriz[2][2] == 'o'):
        print(player2 + ' wins')
        return 2
    elif (matriz[0][2] == 'o' and matriz[1][1] == 'o' and matriz[2][0] == 'o'):
        print(player2 + ' wins')
        return 2
    else:
        if (i == 9):
            print('We have a draw')
            return 0


main()
