import math

from agents.agent_minimax import is_result_better
from agents.agent_minimax.common import DEPTH
from agents.common import PLAYER1, PLAYER2


def test_is_result_better_PLAYER1_true():
    best_score = -math.inf
    best_num_moves = DEPTH
    tmp_score = 1000
    tmp_num_moves = DEPTH

    assert is_result_better(best_score, best_num_moves, tmp_score, tmp_num_moves, PLAYER1) == True
    assert is_result_better(best_score, best_num_moves, tmp_score, tmp_num_moves, PLAYER2) == False


def test_is_result_better_PLAYER2_true():
    best_score = math.inf
    best_num_moves = DEPTH
    tmp_score = -1000
    tmp_num_moves = DEPTH

    assert is_result_better(best_score, best_num_moves, tmp_score, tmp_num_moves, PLAYER2) == True
    assert is_result_better(best_score, best_num_moves, tmp_score, tmp_num_moves, PLAYER1) == False


def test_is_result_better_PLAYER1_tmpScoreLower_numMovesEqual_false():
    best_score = 1000
    best_num_moves = DEPTH
    tmp_score = 999
    tmp_num_moves = DEPTH

    assert is_result_better(best_score, best_num_moves, tmp_score, tmp_num_moves, PLAYER1) == False


def test_is_result_better_PLAYER2_tmpScoreHigher_numMovesEqual_false():
    best_score = 999
    best_num_moves = DEPTH
    tmp_score = 1000
    tmp_num_moves = DEPTH

    assert is_result_better(best_score, best_num_moves, tmp_score, tmp_num_moves, PLAYER2) == False


def test_is_result_better_scoresEqual_numMovesEqual_false():
    best_score = 1000
    best_num_moves = DEPTH
    tmp_score = 1000
    tmp_num_moves = DEPTH

    assert is_result_better(best_score, best_num_moves, tmp_score, tmp_num_moves, PLAYER1) == False
    assert is_result_better(best_score, best_num_moves, tmp_score, tmp_num_moves, PLAYER2) == False


# TODO: figure out if needed
def test_is_result_better_scoresEqual_numMovesLower_true():
    best_score = 1000
    best_num_moves = 4
    tmp_score = 1000
    tmp_num_moves = 3

    assert is_result_better(best_score, best_num_moves, tmp_score, tmp_num_moves, PLAYER1) == True
    assert is_result_better(best_score, best_num_moves, tmp_score, tmp_num_moves, PLAYER2) == True


def test_is_result_better_scoresEqual_numMovesHigher_false():
    best_score = 1000
    best_num_moves = 4
    tmp_score = 1000
    tmp_num_moves = 5

    assert is_result_better(best_score, best_num_moves, tmp_score, tmp_num_moves, PLAYER1) == False
    assert is_result_better(best_score, best_num_moves, tmp_score, tmp_num_moves, PLAYER2) == False
