def scheduler(teams):
    """Round robin scheduling algorithm
    """
    number_of_rounds = len(teams) - 1
    game_per_round = int(len(teams) / 2)
    matches = {}
    for round in range(number_of_rounds):
        games = []
        polar = teams[round]
        games.append((polar, teams[-1]))

        for idx in range(1, game_per_round):
            home = round - idx
            away = round + idx if round + idx < len(teams)-1 else (round + idx) - (len(teams) - 1)
            games.append((teams[:len(teams)-1][home], teams[:len(teams)-1][away],))

        matches.update({round: games})

    return matches
