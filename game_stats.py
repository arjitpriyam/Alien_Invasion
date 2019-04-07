from database import Database

db=Database()

class GameStats():
    def __init__(self, ai_settings,username):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.initial_score=db.get_highscore(username)
        self.high_score = self.initial_score
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1


