from PlayerDatabase import PlayerDatabase


def main() -> None:
    n_players: int = int(input('Enter the number of players: '))

    players = PlayerDatabase(n_players)
    print(players)


if __name__ == '__main__':
    main()
