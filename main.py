from game import BlackJack, Player


def main() -> None:
    player_n = int(input('Enter the number of players: '))
    players = [
        Player(input(f"Enter player {num + 1}'s name: "))
        for num in range(player_n)
    ]
    BlackJack(players).multi_game(int(input('Number of games to play: ')))


if __name__ == '__main__':
    main()
