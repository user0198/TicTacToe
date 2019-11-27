board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def paintBoard(board):
    print(" 1 | 2 | 3\n 4 | 5 | 6\n 7 | 8 | 9\n")
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-' * 11)
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-' * 11)
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def isSpaceFree(pos):
    return board[pos] == ' '


def isWinner(board, le):
    return (
        (board[1] == le and board[2] == le and board[3] == le) or   # horz up
        (board[4] == le and board[5] == le and board[6] == le) or   # horz mid
        (board[7] == le and board[8] == le and board[9] == le) or   # horz bott
        (board[1] == le and board[4] == le and board[7] == le) or   # vert left
        (board[2] == le and board[5] == le and board[8] == le) or   # vert mid
        (board[3] == le and board[6] == le and board[9] == le) or   # vert right
        (board[1] == le and board[5] == le and board[9] == le) or   # main diag
        (board[3] == le and board[5] == le and board[7] == le)  # reverse diag
    )


def isFreeBoard(board):
    return board.count(' ') > 1


def playerMove(letter):
    run = True
    while run:
        move = input(
            'Type your move within a range of (1-9): ')
        try:
            move = int(move)
            if move in range(1, 10):
                if isSpaceFree(move):
                    run = False
                    insertLetter(letter, move)
                else:
                    print('Cell is occupied!')
            else:
                print('Your move has to belong the range!')
        except:
            if move == 'end':
                print('Coward!')
                exit()
            else:
                print('Move should be a number!')


def aiMove(letter):
    possibleMoves = [x for x, letter in enumerate(
        board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    if 5 in possibleMoves:
        move = 5
        return move

    cornersOpen = [x for x in possibleMoves if x in [1, 3, 7, 9]]

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    edgesOpen = [x for x in possibleMoves if x in [2, 4, 6, 8]]

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def clear():
    import os
    os.system('cls')
    return print('Tic Tac Toe Game in progress...')


def main():
    print('Welcome to TicTacToe game!\n(Type "end" to exit)')
    print(" 1 | 2 | 3\n 4 | 5 | 6\n 7 | 8 | 9\n")

    while isFreeBoard(board):
        if not(isWinner(board, 'O')):
            playerMove('X')
            # paintBoard(board)
        else:
            print("\nO's won the game! GG!")
            break

        if not(isWinner(board, 'X')):
            move = aiMove('O')
            if move > 0:
                insertLetter('O', move)
                clear()
                print('AI made move in possition #', move)
                paintBoard(board)
            else:
                print('\nTie Game!')
        else:
            print("\nYou won the game! Well played!")
            break


main()
