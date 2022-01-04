from agents.agent_minimax import determine_num_windows_for_antidiagonal
from agents.common import initialize_game_state

num_windows_dict_rowLastRow = {
    0: 3,
    1: 3,
    2: 2,
    3: 1,
    4: 0,
    5: 0,
    6: 0
}

num_windows_dict_colZero = {
    0: 0,
    1: 0,
    2: 0,
    3: 1,
    4: 2,
    5: 3,
}


def test_determine_num_of_windows_antidiagonal_rowLastRow():
    game = initialize_game_state()
    game_rows = game.shape[0]
    game_cols = game.shape[1]

    for start_col in range(0, game_cols):
        start_row = game_rows - 1

        num_windows = determine_num_windows_for_antidiagonal(game, start_col, start_row)
        assert num_windows == num_windows_dict_rowLastRow.get(start_col)


def test_determine_num_of_windows_antidiagonal_colZero():
    game = initialize_game_state()
    game_rows = game.shape[0]

    for start_row in range(0, game_rows):
        start_col = 0

        num_windows = determine_num_windows_for_antidiagonal(game, start_col, start_row)
        assert num_windows == num_windows_dict_colZero.get(start_row)
