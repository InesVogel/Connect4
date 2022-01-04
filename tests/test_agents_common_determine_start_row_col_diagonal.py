from agents.common import initialize_game_state, determine_start_row_col_for_diagonal


def test_determine_start_rowZero_col_for_diagonal():
    game = initialize_game_state()
    game_rows = game.shape[0]
    game_cols = game.shape[1]

    for action in range(0, game_cols):
        for i in range(0, game_cols):
            last_action = i + action
            last_row = i

            if i <= game_rows:
                row, col = determine_start_row_col_for_diagonal(last_action, last_row)
                assert row == 0
                assert col == action


def test_determine_start_row_colZero_for_diagonal():
    game = initialize_game_state()
    game_rows = game.shape[0]
    game_cols = game.shape[1]

    for i in range(1, game_rows):
        for action in range(0, game_cols):
            last_action = action
            last_row = i + action

            if i <= game_rows:
                row, col = determine_start_row_col_for_diagonal(last_action, last_row)
                assert row == i
                assert col == 0
