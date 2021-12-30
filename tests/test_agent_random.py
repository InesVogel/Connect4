import numpy as np

from agents.agent_random import generate_move


def test_generate_move_random1():
    # Test: random generator only produces numbers between 0 and 6
    from agents.common import initialize_game_state, PLAYER1

    game = initialize_game_state()

    for i in range(100000):
        action = generate_move(game, PLAYER1)[0]
        assert action in (0, 1, 2, 3, 4, 5, 6)


def test_generate_move_random2():
    # Test: random generator produces all numbers between 0 and 6
    from agents.common import initialize_game_state, PLAYER1

    game = initialize_game_state()

    actions = np.zeros((7))
    print(actions)
    for i in range(100000):
        action = generate_move(game, PLAYER1)[0]
        if actions[action] == 0:
            actions[action] = 1

    assert actions.sum() == 7


def test_generate_move_random3():
    # Test: random generator chooses non-full column
    from agents.common import initialize_game_state, PLAYER1, apply_player_action

    game = initialize_game_state()

    for col in range(len(game[0])):
        game = initialize_game_state()
        for row in range(len(game)):
            apply_player_action(game, col, PLAYER1)

        for i in range(100000):
            action = generate_move(game, PLAYER1)[0]
            assert col != action
