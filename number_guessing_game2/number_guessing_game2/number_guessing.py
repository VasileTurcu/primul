import random
from colorama import Fore, init

init(autoreset=True)

class NumberGuessingGame:
    def __init__(self, player):
        self.player = player
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 0

    def choose_difficulty(self):
        print("\nAlege dificultatea:")
        print("1. Easy (10 incercari)")
        print("2. Medium (5 incercari)")
        print("3. Hard (3 incercari)")

        while True:
            try:
                choice = int(input("Introdu alegerea (1-3): "))
                if choice == 1:
                    self.max_attempts = 10
                    break
                elif choice == 2:
                    self.max_attempts = 5
                    break
                elif choice == 3:
                    self.max_attempts = 3
                    break
                else:
                    print(Fore.RED + "Te rog alege 1, 2 sau 3.")
            except ValueError:
                print(Fore.RED + "Introdu un numar valid!")

    def play(self):
        self.choose_difficulty()
        print(Fore.CYAN + "\nSa incepem jocul! Ghici numarul intre 1 si 100.\n")

        while self.attempts < self.max_attempts:
            try:
                guess = int(input("Introdu numarul: "))
            except ValueError:
                print(Fore.RED + "Introdu un numar valid!")
                continue

            self.attempts += 1

            if guess == self.secret_number:
                print(Fore.GREEN + f"🎉 Felicitari! Ai ghicit in {self.attempts} incercari!")
                self.player.add_win()
                return True
            elif guess > self.secret_number:
                print(Fore.YELLOW + "Numarul este mai mic!")
            else:
                print(Fore.YELLOW + "Numarul este mai mare!")

        print(Fore.RED + f"\n😞 Ai pierdut! Numarul era {self.secret_number}.")
        self.player.add_loss()
        return False