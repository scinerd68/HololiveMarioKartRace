def get_expected_score(player, opponents):
    """
    Return expected score of a player given their opponents
    Expected score in [0, 1]
    """
    score = 0

    for opponent in opponents:
        score += 1 / (1 + 10**((opponent.current_elo - player.current_elo) / 400))

    score /= (len(opponents) * (len(opponents) + 1) / 2)
    return score

def get_real_scores(num_players):
    """
    Return a list of scores that each gain based on their postion, following Mario Kart system
    (0th element correspond to score of 1st place etc...)
    """
    if num_players == 12:
        scores = [15, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    elif num_players == 11:
        scores = [13, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    elif num_players == 8:
        scores = [10, 8, 6, 5, 4, 3, 2, 1]
    elif num_players == 2:
        scores = [3, 1]

    return scores


def get_game_scores(num_players):
    """
    From real scores calculate game scores to calculate elo
    """
    # scores = get_real_scores(num_players)
    # # Normalize to [0, 1]
    # scores = [(score - min(scores)) / (max(scores) - min(scores)) for score in scores]
    scores = []
    for position in range(1, num_players+1):
        score = (num_players - position) / (num_players * (num_players - 1) / 2)
        scores.append(score)
    return scores


def get_individual_rating_change(game_score, expected_score, num_players, k=32):
    """
    game_score: [0, 1]
    expected_score: [0, 1]
    """
    return k * (num_players - 1) * (game_score - expected_score)


def get_all_ratings_change(players_list):
    """
    players_list: List of players in the order of finishing first to last
    return list rating change of each player in order
    """
    all_game_scores = get_game_scores(len(players_list))
    all_ratings_change = []

    for player_position, player in enumerate(players_list):
        opponents = set(players_list) - {player}
        player_expected_score = get_expected_score(player, opponents)
        player_game_score = all_game_scores[player_position]
        player_rating_change = get_individual_rating_change(player_game_score, player_expected_score,
                                                            len(players_list))
        all_ratings_change.append(player_rating_change)
    
    return all_ratings_change
