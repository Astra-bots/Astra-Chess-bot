import chess

WHITE = "⬜"
BLACK = "⬛"

PIECES = {
    "P": "♙",
    "N": "♘",
    "B": "♗",
    "R": "♖",
    "Q": "♕",
    "K": "♔",

    "p": "♟",
    "n": "♞",
    "b": "♝",
    "r": "♜",
    "q": "♛",
    "k": "♚"
}


def square_text(board, square):

    piece = board.piece_at(square)

    if piece:

        return PIECES[piece.symbol()]

    rank = chess.square_rank(square)
    file = chess.square_file(square)

    if (rank + file) % 2 == 0:
        return WHITE

    return BLACK


def board_keyboard(board):

    keyboard = []

    for rank in range(7, -1, -1):

        row = []

        for file in range(8):

            square = chess.square(file, rank)

            row.append(
                {
                    "text": square_text(board, square),
                    "square": square
                }
            )

        keyboard.append(row)

    return keyboard
