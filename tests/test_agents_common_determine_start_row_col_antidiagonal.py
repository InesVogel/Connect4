from agents.common import initialize_game_state, determine_start_row_col_for_antidiagonal


def test_determine_start_rowZero_col_for_antidiagonal():
    game = initialize_game_state()
    game_rows = game.shape[0]
    game_cols = game.shape[1]

    for i in range(1, game_cols):
        row_counter = 1
        for action in range(i, game_cols):
            last_action = action
            last_row = game_rows - row_counter

            if i <= game_rows:
                row, col = determine_start_row_col_for_antidiagonal(game, last_action, last_row)
                assert row == game_rows - 1
                assert col == i

            row_counter = row_counter + 1


def test_determine_start_row_colZero_for_antidiagonal():
    game = initialize_game_state()
    game_rows = game.shape[0]
    game_cols = game.shape[1]

    for i in range(0, game_rows):
        for action in range(0, game_cols):
            last_action = action
            last_row = i - action

            if i <= game_rows:
                row, col = determine_start_row_col_for_antidiagonal(game, last_action, last_row)
                assert row == i
                assert col == 0
