import chess

from ai import ChessAI
from score import Score





class ChessGame:


    def __init__(self):

        self.board = chess.Board()

        self.ai = ChessAI()

        self.score = Score()

        self.selected = None






    def reset(self):

        self.board.reset()

        self.selected = None






    def player_move(self, start, end):


        move = chess.Move(

            start,

            end

        )


        if move in self.board.legal_moves:


            self.board.push(move)

            return True



        return False








    def bot_move(self):


        if self.board.is_game_over():

            return None



        move = self.ai.choose_move(

            self.board

        )


        if move:


            self.board.push(move)


            return move



        return None







    def game_status(self):


        if self.board.is_checkmate():

            if self.board.turn == chess.WHITE:

                return "Bot Wins"

            else:

                return "Player Wins"




        if self.board.is_stalemate():

            return "Draw"



        if self.board.is_insufficient_material():

            return "Draw"



        return "Playing"
