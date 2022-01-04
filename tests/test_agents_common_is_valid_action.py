import numpy as np

from agents.common import PLAYER1, PLAYER2, NO_PLAYER, initialize_game_state, is_valid_action


def test_valid_action_allValid():
    game = initialize_game_state()

    for i in {0, 1, 2, 3, 4, 5, 6}:
        assert is_valid_action(game, i) == True


def test_valid_action_oneValid_Column6():
    game = initialize_game_state()
    game[-1] = np.array([PLAYER1, PLAYER1, PLAYER1, PLAYER1, PLAYER1, PLAYER1, NO_PLAYER])

    for i in {0, 1, 2, 3, 4, 5}:
        assert is_valid_action(game, i) == False

    for i in {6}:
        assert is_valid_action(game, i) == True


def test_valid_action_oneValid_Column5():
    game = initialize_game_state()
    game[-1] = np.array([PLAYER1, PLAYER1, PLAYER1, PLAYER1, PLAYER1, NO_PLAYER, PLAYER1])

    for i in {0, 1, 2, 3, 4, 6}:
        assert is_valid_action(game, i) == False

    for i in {5}:
        assert is_valid_action(game, i) == True


def test_valid_action_oneValid_Column4():
    game = initialize_game_state()
    game[-1] = np.array([PLAYER1, PLAYER1, PLAYER1, PLAYER1, NO_PLAYER, PLAYER1, PLAYER1])

    for i in {0, 1, 2, 3, 5, 6}:
        assert is_valid_action(game, i) == False

    for i in {4}:
        assert is_valid_action(game, i) == True


def test_valid_action_oneValid_Column3():
    game = initialize_game_state()
    game[-1] = np.array([PLAYER1, PLAYER1, PLAYER1, NO_PLAYER, PLAYER1, PLAYER1, PLAYER1])

    for i in {0, 1, 2, 4, 5, 6}:
        assert is_valid_action(game, i) == False

    for i in {3}:
        assert is_valid_action(game, i) == True


def test_valid_action_oneValid_Column2():
    game = initialize_game_state()
    game[-1] = np.array([PLAYER1, PLAYER1, NO_PLAYER, PLAYER1, PLAYER1, PLAYER1, PLAYER1])

    for i in {0, 1, 3, 4, 5, 6}:
        assert is_valid_action(game, i) == False

    for i in {2}:
        assert is_valid_action(game, i) == True


def test_valid_action_oneValid_Column1():
    game = initialize_game_state()
    game[-1] = np.array([PLAYER1, NO_PLAYER, PLAYER1, PLAYER1, PLAYER1, PLAYER1, PLAYER1])

    for i in {0, 2, 3, 4, 5, 6}:
        assert is_valid_action(game, i) == False

    for i in {1}:
        assert is_valid_action(game, i) == True


def test_valid_action_oneValid_Column0():
    game = initialize_game_state()
    game[-1] = np.array([NO_PLAYER, PLAYER1, PLAYER1, PLAYER1, PLAYER1, PLAYER1, PLAYER1])

    for i in {1, 2, 3, 4, 5, 6}:
        assert is_valid_action(game, i) == False

    for i in {0}:
        assert is_valid_action(game, i) == True


def test_valid_action_twoValid_Col_16():
    game = initialize_game_state()
    game[-1] = np.array([PLAYER2, NO_PLAYER, PLAYER1, PLAYER1, PLAYER2, PLAYER1, NO_PLAYER])

    for i in {0, 2, 3, 4, 5}:
        assert is_valid_action(game, i) == False

    for i in {1, 6}:
        assert is_valid_action(game, i) == True


def test_valid_action_threeValid_Col_156():
    game = initialize_game_state()
    game[-1] = np.array([PLAYER2, NO_PLAYER, PLAYER1, PLAYER1, PLAYER2, NO_PLAYER, NO_PLAYER])

    for i in {0, 2, 3, 4}:
        assert is_valid_action(game, i) == False

    for i in {1, 5, 6}:
        assert is_valid_action(game, i) == True


def test_valid_action_fourValid_Col_0156():
    game = initialize_game_state()
    game[-1] = np.array([NO_PLAYER, NO_PLAYER, PLAYER1, PLAYER1, PLAYER2, NO_PLAYER, NO_PLAYER])

    for i in {2, 3, 4}:
        assert is_valid_action(game, i) == False

    for i in {0, 1, 5, 6}:
        assert is_valid_action(game, i) == True


def test_valid_action_fiveValid_Col_01356():
    game = initialize_game_state()
    game[-1] = np.array([NO_PLAYER, NO_PLAYER, PLAYER1, NO_PLAYER, PLAYER2, NO_PLAYER, NO_PLAYER])

    for i in {2, 4}:
        assert is_valid_action(game, i) == False

    for i in {0, 1, 3, 5, 6}:
        assert is_valid_action(game, i) == True


def test_valid_action_sixValid_Col_012345():
    game = initialize_game_state()
    game[-1] = np.array([NO_PLAYER, NO_PLAYER, NO_PLAYER, NO_PLAYER, NO_PLAYER, NO_PLAYER, PLAYER1])

    for i in {6}:
        assert is_valid_action(game, i) == False

    for i in {0, 1, 2, 3, 4, 5}:
        assert is_valid_action(game, i) == True


def test_valid_action_sixValid_Col_012346():
    game = initialize_game_state()
    game[-1] = np.array([NO_PLAYER, NO_PLAYER, NO_PLAYER, NO_PLAYER, NO_PLAYER, PLAYER2, NO_PLAYER])

    for i in {5}:
        assert is_valid_action(game, i) == False

    for i in {0, 1, 2, 3, 4, 6}:
        assert is_valid_action(game, i) == True


def test_valid_action_sixValid_Col_012356():
    game = initialize_game_state()
    game[-1] = np.array([NO_PLAYER, NO_PLAYER, NO_PLAYER, NO_PLAYER, PLAYER2, NO_PLAYER, NO_PLAYER])

    for i in {4}:
        assert is_valid_action(game, i) == False

    for i in {0, 1, 2, 3, 5, 6}:
        assert is_valid_action(game, i) == True


def test_valid_action_sixValid_Col_012456():
    game = initialize_game_state()
    game[-1] = np.array([NO_PLAYER, NO_PLAYER, NO_PLAYER, PLAYER2, NO_PLAYER, NO_PLAYER, NO_PLAYER])

    for i in {3}:
        assert is_valid_action(game, i) == False

    for i in {0, 1, 2, 4, 5, 6}:
        assert is_valid_action(game, i) == True


def test_valid_action_sixValid_Col_013456():
    game = initialize_game_state()
    game[-1] = np.array([NO_PLAYER, NO_PLAYER, PLAYER1, NO_PLAYER, NO_PLAYER, NO_PLAYER, NO_PLAYER])

    for i in {2}:
        assert is_valid_action(game, i) == False

    for i in {0, 1, 3, 4, 5, 6}:
        assert is_valid_action(game, i) == True


def test_valid_action_sixValid_Col_023456():
    game = initialize_game_state()
    game[-1] = np.array([NO_PLAYER, PLAYER2, NO_PLAYER, NO_PLAYER, NO_PLAYER, NO_PLAYER, NO_PLAYER])

    for i in {1}:
        assert is_valid_action(game, i) == False

    for i in {0, 2, 3, 4, 5, 6}:
        assert is_valid_action(game, i) == True


def test_valid_action_sixValid_Col_123456():
    game = initialize_game_state()
    game[-1] = np.array([PLAYER2, NO_PLAYER, NO_PLAYER, NO_PLAYER, NO_PLAYER, NO_PLAYER, NO_PLAYER])

    for i in {0}:
        assert is_valid_action(game, i) == False

    for i in {1, 2, 3, 4, 5, 6}:
        assert is_valid_action(game, i) == True


def test_valid_action_noneValid_mixedPlayer():
    game = initialize_game_state()
    game[-1] = np.array([PLAYER2, PLAYER2, PLAYER1, PLAYER1, PLAYER2, PLAYER1, PLAYER1])

    for i in {0, 1, 2, 3, 4, 5, 6}:
        assert is_valid_action(game, i) == False


def test_valid_action_noneValid_singlePlayer2():
    game = initialize_game_state()
    game[-1] = np.array([PLAYER2, PLAYER2, PLAYER2, PLAYER2, PLAYER2, PLAYER2, PLAYER2])

    for i in {0, 1, 2, 3, 4, 5, 6}:
        assert is_valid_action(game, i) == False


def test_valid_action_noneValid_singlePlayer1():
    game = initialize_game_state()
    game[-1] = np.array([PLAYER1, PLAYER1, PLAYER1, PLAYER1, PLAYER1, PLAYER1, PLAYER1])

    for i in {0, 1, 2, 3, 4, 5, 6}:
        assert is_valid_action(game, i) == False


def test_valid_action_actionOutOfBounds():
    game = initialize_game_state()

    for i in {0, 1, 2, 3, 4, 5, 6}:
        assert is_valid_action(game, i) == True

    for i in {-1, 7}:
        assert is_valid_action(game, i) == False
