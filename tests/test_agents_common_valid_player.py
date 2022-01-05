from agents.common import NO_PLAYER, PLAYER1, PLAYER2, valid_player


def test_valid_player_True():
    assert valid_player(NO_PLAYER) == True
    assert valid_player(PLAYER1) == True
    assert valid_player(PLAYER2) == True


def test_valid_player_False():
    assert valid_player(3) == False
    assert valid_player(-1) == False
