from agents.common import initialize_game_state, valid_action


def test_valid_action_True():
    game = initialize_game_state()

    for i in range(0, len(game)):
        assert valid_action(game, i) == True


def test_valid_action_False():
    game = initialize_game_state()

    assert valid_action(game, -1) == False
    assert valid_action(game, 7) == False
    assert valid_action(game, 15) == False
