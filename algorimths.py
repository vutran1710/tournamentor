def round_robin_scheduler(teams: list) -> dict:
    """Round robin scheduling algorithm
    """
    if len(teams) % 2 != 0:
        """If number of teams is odd, we add a fake Team to the existing team list
        """
        teams.append(None)

    number_of_rounds = len(teams) - 1
    game_per_round = int(len(teams) / 2)
    matches = {}

    for round in range(number_of_rounds):
        games = []

        if teams[-1] is not None:
            games.append((teams[round], teams[-1]))

        for idx in range(1, game_per_round):
            home = round - idx
            away = round + idx if round + idx < len(teams)-1 else (round + idx) - (len(teams) - 1)
            games.append((teams[:len(teams)-1][home], teams[:len(teams)-1][away],))

        matches.update({round: games})

    return matches
