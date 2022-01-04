import numpy as np

from agents.agent_minimax import is_player_blocking_opponent
from agents.common import PLAYER1, PLAYER2, NO_PLAYER


def test_is_player_blocking_opponent_2blocks1():
    window = np.array([PLAYER1, PLAYER1, PLAYER1, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER1) == False
    assert is_player_blocking_opponent(window, PLAYER2) == True

    window = np.array([PLAYER1, PLAYER1, PLAYER2, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER1) == False
    assert is_player_blocking_opponent(window, PLAYER2) == True

    window = np.array([PLAYER1, PLAYER2, PLAYER1, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER1) == False
    assert is_player_blocking_opponent(window, PLAYER2) == True

    window = np.array([PLAYER2, PLAYER1, PLAYER1, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER1) == False
    assert is_player_blocking_opponent(window, PLAYER2) == True


def test_is_player_blocking_opponent_1blocks2():
    window = np.array([PLAYER2, PLAYER2, PLAYER2, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == True

    window = np.array([PLAYER2, PLAYER2, PLAYER1, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == True

    window = np.array([PLAYER2, PLAYER1, PLAYER2, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == True

    window = np.array([PLAYER1, PLAYER2, PLAYER2, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == True


def test_is_player_blocking_opponent_false_singleFieldOccupied_singlePlayer():
    window = np.array([PLAYER2, NO_PLAYER, NO_PLAYER, NO_PLAYER])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([NO_PLAYER, PLAYER2, NO_PLAYER, NO_PLAYER])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([NO_PLAYER, NO_PLAYER, PLAYER2, NO_PLAYER])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([NO_PLAYER, NO_PLAYER, NO_PLAYER, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER1, NO_PLAYER, NO_PLAYER, NO_PLAYER])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([NO_PLAYER, PLAYER1, NO_PLAYER, NO_PLAYER])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([NO_PLAYER, NO_PLAYER, PLAYER1, NO_PLAYER])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([NO_PLAYER, NO_PLAYER, NO_PLAYER, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False


def test_is_player_blocking_opponent_false_twoFieldsOccupied_singlePlayer():
    window = np.array([PLAYER2, PLAYER2, NO_PLAYER, NO_PLAYER])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER2, NO_PLAYER, NO_PLAYER, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([NO_PLAYER, NO_PLAYER, PLAYER2, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER1, PLAYER1, NO_PLAYER, NO_PLAYER])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER1, NO_PLAYER, NO_PLAYER, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([NO_PLAYER, NO_PLAYER, PLAYER1, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False


def test_is_player_blocking_opponent_false_twoFieldsOccupied_multiplePlayer():
    window = np.array([PLAYER2, PLAYER1, NO_PLAYER, NO_PLAYER])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER1, PLAYER2, NO_PLAYER, NO_PLAYER])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER2, NO_PLAYER, NO_PLAYER, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER1, NO_PLAYER, NO_PLAYER, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([NO_PLAYER, NO_PLAYER, PLAYER1, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([NO_PLAYER, NO_PLAYER, PLAYER2, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False


def test_is_player_blocking_opponent_false_threeFieldsOccupied_singlePlayer():
    window = np.array([PLAYER2, PLAYER2, PLAYER2, NO_PLAYER])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER2, PLAYER2, NO_PLAYER, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER2, NO_PLAYER, PLAYER2, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([NO_PLAYER, PLAYER2, PLAYER2, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER1, PLAYER1, PLAYER1, NO_PLAYER])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER1, PLAYER1, NO_PLAYER, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER1, NO_PLAYER, PLAYER1, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([NO_PLAYER, PLAYER1, PLAYER1, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False


def test_is_player_blocking_opponent_false_threeFieldsOccupied_multiplePlayer():
    window = np.array([PLAYER1, PLAYER2, PLAYER2, NO_PLAYER])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER2, PLAYER1, NO_PLAYER, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER2, NO_PLAYER, PLAYER2, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([NO_PLAYER, PLAYER1, PLAYER2, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER1, PLAYER1, PLAYER2, NO_PLAYER])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER2, PLAYER1, NO_PLAYER, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER1, NO_PLAYER, PLAYER1, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([NO_PLAYER, PLAYER1, PLAYER2, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False


def test_is_player_blocking_opponent_false_fourFieldsOccupied_singlePlayer():
    window = np.array([PLAYER2, PLAYER2, PLAYER2, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER1, PLAYER1, PLAYER1, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False


def test_is_player_blocking_opponent_false_fourFieldsOccupied_multiplePlayer():
    window = np.array([PLAYER1, PLAYER1, PLAYER2, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER2, PLAYER2, PLAYER1, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER1, PLAYER2, PLAYER2, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER2, PLAYER1, PLAYER1, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER2, PLAYER1, PLAYER2, PLAYER1])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False

    window = np.array([PLAYER1, PLAYER2, PLAYER1, PLAYER2])
    assert is_player_blocking_opponent(window, PLAYER2) == False
    assert is_player_blocking_opponent(window, PLAYER1) == False
