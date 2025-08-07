

from number_guessing_game2.player import Player
from number_guessing_game2.number_guessing import NumberGuessingGame
from number_guessing_game2.leaderboard import Leaderboard
from number_guessing_game2.api_service import ApiService



def main():
    print("=== Jocul Ghicit Număr 2.0 ===")
    name = input("Introdu numele tău: ")
    player = Player(name)
    leaderboard = Leaderboard()
    api_service = ApiService()

    while True:
        game = NumberGuessingGame(player)
        game.play()
        leaderboard.update(player)

        # Afișează leaderboard
        print("\nClasament:")
        leaderboard.show()

        # Trimite scorul la API (exemplu)
        api_service.send_score(player.name, player.wins, player.losses)

        again = input("\nVrei să joci din nou? (da/nu): ").strip().lower()
        if again != 'da':
            print("Mulțumesc pentru joc!")
            break


if __name__ == "__main__":
    main()
