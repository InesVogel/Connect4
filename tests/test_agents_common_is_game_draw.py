import random

from agents.common import PLAYER1, PLAYER2, initialize_game_state, is_game_draw


def test_is_game_draw_True():
    for num_tests in range(1, 100):
        game = initialize_game_state()
        for i in range(0, game.shape[1]):
            game[-1][i] = random.choice([PLAYER1, PLAYER2])

        assert is_game_draw(game) == True


def test_is_game_draw_False_oneFieldNotOccupied():
    num_cols = 7

    for num_tests in range(1, 100):
        for col in range(0, num_cols):
            game = initialize_game_state()
            for i in range(0, game.shape[1]):
                if i != col:
                    game[-1][i] = random.choice([PLAYER1, PLAYER2])

            assert is_game_draw(game) == False


def test_is_game_draw_False_twoFieldsNotOccupied():
    num_cols = 7

    for num_tests in range(1, 2):
        for col in range(0, num_cols):
            second_col = num_cols - col - 1
            game = initialize_game_state()
            for i in range(0, game.shape[1]):
                if i != col and i != second_col:
                    game[-1][i] = random.choice([PLAYER1, PLAYER2])

            assert is_game_draw(game) == False
