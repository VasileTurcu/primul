class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0

    def add_win(self):
        self.wins += 1

    def add_loss(self):
        self.losses += 1

    def get_stats(self):
        return f"{self.name} - Wins: {self.wins}, Losses: {self.losses}"