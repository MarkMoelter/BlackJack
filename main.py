from game import BlackJack, Player


def int_above_0(raw_input: str) -> int:
    """Convert an input string to an int that must be greater than 0."""
    # verify it's a digit
    if not raw_input.isdigit():
        raise ValueError('Input value must be a number')

    # verify it's greater than 0
    if int(raw_input) <= 0:
        raise ValueError('Input value must be greater than zero')

    return int(raw_input)


def main() -> None:
    num_players_input = input('Enter the number of players: ')
    num_games_input = input('Enter the number of games to play: ')

    players = [
        Player(input(f"Enter player {num + 1}'s name: "))
        for num in range(int_above_0(num_players_input))
    ]
    BlackJack(players).multi_game(int_above_0(num_games_input))


if __name__ == '__main__':
    main()
