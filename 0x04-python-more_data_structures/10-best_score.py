#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    biggest_score = None
    biggest_score_key = None
    for key, value in a_dictionary.items():
        if biggest_score is None or value > biggest_score:
            biggest_score = value
            biggest_score_key = key
    return biggest_score_key
