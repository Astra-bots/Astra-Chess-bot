class Score:


    def __init__(self):

        self.player = 0

        self.bot = 0





    def player_win(self):

        self.player += 1





    def bot_win(self):

        self.bot += 1





    def get_score(self):

        return {

            "Player": self.player,

            "Bot": self.bot

        }





    def reset(self):

        self.player = 0

        self.bot = 0
