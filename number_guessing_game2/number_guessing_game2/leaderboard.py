class Leaderboard:
    def __init__(self):
        self.players = []

    def update(self, player):
        self.players.append({
            "name": player.name,
            "wins": player.wins,
            "losses": player.losses
        })

    def display(self):
        print("\n🏆 Clasament jucători 🏆")
        for i, player in enumerate(self.players, 1):
            print(f"{i}. {player['name']} - Victorii: {player['wins']} | Înfrângeri: {player['losses']}")

    def show(self):
        self.display()