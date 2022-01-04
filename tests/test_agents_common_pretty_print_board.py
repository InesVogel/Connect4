from agents.common import initialize_game_state, pretty_print_board


def test_pretty_print_board_empty():
    print_board = pretty_print_board(initialize_game_state()).replace("\n", "")

    expected_board = "|==============|" \
                     "|              |" \
                     "|              |" \
                     "|              |" \
                     "|              |" \
                     "|              |" \
                     "|              |" \
                     "|==============|" \
                     "|0 1 2 3 4 5 6 |".replace("\n", "")

    assert print_board == expected_board
