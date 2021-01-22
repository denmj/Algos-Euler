"""

Given the positions of a white bishop and a black pawn on the standard chess board,
determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement.
Check out the example below to see how it can move:

For bishop = "a1" and pawn = "c3", the output should be
bishopAndPawn(bishop, pawn) = true

"""


def bishopAndPawn(bishop, pawn):

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numbs = ['1', '2', '3', '4', '5', '6', '7', '8']
    moves = []
    board = [[l + n for n in numbs] for l in letters]

    for pos_ in (pawn, bishop):
        for inx1, row, in enumerate(board):
            if pos_ in row:
                print("Coordinates of the figure: ({}, {})".format(inx1 + 1, row.index(pos_) + 1))
                moves.append([inx1 + 1, row.index(pos_) + 1])
                print("Position on board: {}".format(pos_))
    if abs(moves[1][0] - moves[0][0]) == abs(moves[1][1] - moves[0][1]) and abs(moves[1][1] - moves[0][1]) > 0:
        return True
    else:
        return False






