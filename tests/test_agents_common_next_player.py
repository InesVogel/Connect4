from agents.common import PLAYER1, PLAYER2, NO_PLAYER, next_player


def test_next_player_expectedPLAYER1():
    assert next_player(PLAYER2) == PLAYER1


def test_next_player_expectedPLAYER2():
    assert next_player(PLAYER1) == PLAYER2


def test_next_player_expectedNOPLAYER():
    assert next_player(NO_PLAYER) == NO_PLAYER
