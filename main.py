from typing import Tuple
import numpy as np
import sys

legalMoves = {(1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (3, 0), (0, 3), (1, 2), (2, 1)}

board = {(i, j): '' for i in range(0, 11) for j in range(0, 11)}

board[(0, 0)] = "lost"

for couple in legalMoves:
    board[couple] = 'win'

for i in range(11):
    for j in range(11):
        if (i, j) in legalMoves:
            continue
        for move in legalMoves:
            if tuple(np.subtract((i, j), move)) in board:
                if board[tuple(np.subtract((i, j), move))] == 'win':
                    board[(i, j)] = 'lost'
                elif board[tuple(np.subtract((i, j), move))] == 'lost':
                    board[(i, j)] = 'win'
                    break

def getNextStep(computerMove: Tuple[int, int], boardState: Tuple[int, int] = (10, 10)) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    boardState = tuple(np.subtract(boardState, computerMove))

    if board[boardState] == 'lost':
        return ((-1, -1), boardState)
    else:
        for move in legalMoves:
            if tuple(np.subtract(boardState, move)) in board:
                if board[tuple(np.subtract(boardState, move))] == 'lost':
                    boardState = tuple(np.subtract(boardState, move))
                    return (move, boardState)
    return ((-1, -1), boardState)

if __name__ == '__main__':
    computerMove = tuple(map(lambda x: int(x), input("Enter Computer move as x y: ").split()))
    (nextMove, currentBoard) = getNextStep(computerMove)
    print(f"Your Next game should be ({nextMove[0]}, {nextMove[1]})\n")

    while(True):
        computerMove = tuple(map(lambda x: int(x), input("Enter Computer move as x y: ").split()))
        (nextMove, currentBoard) = getNextStep(computerMove, currentBoard)

        if nextMove[0] != -1:
            print(f"Your Next game should be ({nextMove[0]}, {nextMove[1]})\n")
            if currentBoard == (0, 0):
                print("Congratulations! You won the Game!\n")
                sys.exit(0)
        else:
            print("You Lost the Game! If you followed the steps correctly and still lost, please debug the code and make a PR\n")
            sys.exit(0)