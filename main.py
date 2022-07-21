from game import Game, Player


def main() -> None:
    player_n = int(input('Enter the number of players: '))
    players = [
        Player(input(f"Enter player {num + 1}'s name: "))
        for num in range(player_n)
    ]
    Game(players).single_game()


if __name__ == '__main__':
    main()
