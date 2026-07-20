import random
import chess


PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 100
}


class ChessAI:

    def choose_move(self, board):

        legal_moves = list(board.legal_moves)

        if not legal_moves:
            return None

        capture_moves = []

        for move in legal_moves:

            piece = board.piece_at(move.to_square)

            if piece:

                value = PIECE_VALUES.get(
                    piece.piece_type,
                    0
                )

                capture_moves.append(
                    (value, move)
                )

        if capture_moves:

            capture_moves.sort(
                reverse=True,
                key=lambda x: x[0]
            )

            return capture_moves[0][1]

        return random.choice(legal_moves)
