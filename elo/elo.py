import json
from typing import List


def elo_adjust(outcomes: json, current) -> List[dict]:
    """
    Takes in a score dictionary (must be len 2) in the format {key:value, key:value} where key is name
    for each player and value is their score in the game
    Ex. {"Brian": 0, "TylerW":11}
    Ex. {"p1_name": "Brian", "p1_score": 0, "p2_name": "Tyler", "p2_score": 11}
    """

    p1 = outcomes["p1_name"]
    p2 = outcomes["p2_name"]
    p1_score = int(outcomes["p1_score"])
    p2_score = int(outcomes["p2_score"])
    total = p1_score + p2_score
    p1_rating = current["p1_current"]
    p2_rating = current["p2_current"]
    exp1 = (1 / (1 + 10 ** ((p2_rating - p1_rating) / 400))) * total
    exp2 = (1 / (1 + 10 ** ((p1_rating - p2_rating) / 400))) * total
    player_updates = [
        {
            "name": p1,
            "rating": int(round(max(100, p1_rating + 25 * (p1_score - exp1)), 0)),
        },
        {
            "name": p2,
            "rating": int(round(max(100, p2_rating + 25 * (p2_score - exp2)), 0)),
        },
    ]
    return player_updates

