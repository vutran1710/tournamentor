def round_robin_scheduler(teams: list, callback=None) -> dict:
    """Round robin scheduling algorithm
    - Refer to https://en.wikipedia.org/wiki/Round-robin_tournament#Scheduling_algorithm
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
            match = (teams[round], teams[-1],)
            games.append(match) if not callback else callback(match, round)

        for idx in range(1, game_per_round):
            home = round - idx
            away = round + idx if round + idx < len(teams)-1 else (round + idx) - (len(teams) - 1)
            home_team = teams[:len(teams)-1][home]
            away_team = teams[:len(teams)-1][away]
            match = (home_team, away_team,)
            games.append(match) if not callback else callback(match, round)

        if not callback:
            matches.update({round: games})

    if not callback:
        return matches
