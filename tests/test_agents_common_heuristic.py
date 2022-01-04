from agents.common import PLAYER1, PLAYER2, initialize_game_state, apply_player_action, string_to_board, heuristic


def test_heuristic_columnWithZeroOccupiedFields_expectScoreZero():
    game = initialize_game_state()

    score = heuristic(game)

    assert score == 0


def test_heuristic_columnWithOneOccupiedFields_expectScoreZero():
    game = initialize_game_state()

    for i in range(1):
        apply_player_action(game, 0, PLAYER1)

    score = heuristic(game)

    assert score == 0


def test_heuristic_columnWith6OccupiedFields_expectScoreZero():
    game = initialize_game_state()

    for i in range(6):
        apply_player_action(game, 0, PLAYER1)

    score = heuristic(game)

    assert score == 0


def test_heuristic_columnWith4OccupiedFields_differntPlayer_expectScore1100():
    game = initialize_game_state()

    apply_player_action(game, 0, PLAYER2)
    for i in range(1, 4):
        apply_player_action(game, 0, PLAYER1)

    score = heuristic(game)

    assert score == 1100


def test_heuristic_columnWith4OccupiedFields_samePlayer_expectScore1100():
    game = initialize_game_state()

    for i in range(4):
        apply_player_action(game, 0, PLAYER1)

    score = heuristic(game)

    assert score == 1100


def test_heuristic_columnWith3OccupiedFields_differentPlayer_expectScoreZero():
    game = initialize_game_state()

    for i in range(2):
        apply_player_action(game, 0, PLAYER1)

    apply_player_action(game, 0, PLAYER2)

    score = heuristic(game)

    assert score == 0


def test_heuristic_columnWith3OccupiedFields_differentPlayer_expectScore100():
    game = initialize_game_state()

    apply_player_action(game, 0, PLAYER2)
    for i in range(1, 3):
        apply_player_action(game, 0, PLAYER1)

    score = heuristic(game)

    assert score == 100


def test_heuristic_columnWith3OccupiedFields_samePlayer_expectScore1100():
    game = initialize_game_state()

    for i in range(3):
        apply_player_action(game, 0, PLAYER1)

    score = heuristic(game)

    assert score == 1100


def test_heuristic_columnWith2OccupiedFields_samePlayer_expectScore100():
    game = initialize_game_state()

    for i in range(2):
        apply_player_action(game, 0, PLAYER1)

    score = heuristic(game)

    assert score == 100


def test_heuristic_columnWith2OccupiedFields_differentPlayer_expectScoreZero():
    game = initialize_game_state()

    apply_player_action(game, 0, PLAYER2)
    apply_player_action(game, 0, PLAYER1)

    score = heuristic(game)

    assert score == 0


def test_heuristic_columnWith5OccupiedFields_differentPlayer_expectScore1000():
    game = initialize_game_state()

    apply_player_action(game, 0, PLAYER2)
    apply_player_action(game, 0, PLAYER2)
    for i in range(2, 5):
        apply_player_action(game, 0, PLAYER1)

    score = heuristic(game)

    assert score == 1000


def test_heuristic_columnWith5OccupiedFields_differentPlayer_expectScoreZero():
    game = initialize_game_state()

    apply_player_action(game, 0, PLAYER2)
    apply_player_action(game, 0, PLAYER2)
    apply_player_action(game, 0, PLAYER2)
    for i in range(3, 5):
        apply_player_action(game, 0, PLAYER1)

    score = heuristic(game)

    assert score == 0


def test_heuristic_columnWith5OccupiedFields_samePlayer_expectScore1000():
    game = initialize_game_state()

    for i in range(5):
        apply_player_action(game, 0, PLAYER1)

    score = heuristic(game)

    assert score == 1000


def test_heuristic_row0_expectScoreZERO():
    game = initialize_game_state()

    apply_player_action(game, 0, PLAYER1)
    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 2, PLAYER2)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 5, PLAYER1)
    apply_player_action(game, 6, PLAYER2)

    score = heuristic(game)
    assert score == 0


def test_heuristic_row0_expectScore1000():
    game = initialize_game_state()

    apply_player_action(game, 0, PLAYER1)
    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 2, PLAYER2)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 5, PLAYER1)

    score = heuristic(game)
    assert score == 1000


def test_heuristic_row0_expectScore4000():
    game = initialize_game_state()

    apply_player_action(game, 0, PLAYER1)
    apply_player_action(game, 1, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 4, PLAYER1)
    apply_player_action(game, 5, PLAYER1)

    score = heuristic(game)
    assert score == 4000


def test_heuristic_mix_expectScore1000():
    game = initialize_game_state()

    for i in range(0, 7):
        if i == 3:
            apply_player_action(game, i, PLAYER1)
        else:
            apply_player_action(game, i, PLAYER2)

    apply_player_action(game, 0, PLAYER1)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 4, PLAYER2)

    score = heuristic(game)
    assert score == 1000


def test_heuristic_mix_expectScore900():
    game = initialize_game_state()

    for i in range(0, 7):
        apply_player_action(game, i, PLAYER2)

    apply_player_action(game, 0, PLAYER1)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 4, PLAYER2)

    score = heuristic(game)
    assert score == 900


def test_heuristic_row1_expectScoreNegative2200():
    game = initialize_game_state()

    for i in range(0, 7):
        apply_player_action(game, i, PLAYER1)

    apply_player_action(game, 0, PLAYER2)
    apply_player_action(game, 2, PLAYER2)
    apply_player_action(game, 3, PLAYER2)
    apply_player_action(game, 5, PLAYER2)

    score = heuristic(game)
    assert score == -2200


def test_heuristic_row1_expectScoreZero():
    game = initialize_game_state()

    for i in range(0, 7):
        if i == 3:
            apply_player_action(game, i, PLAYER1)
        if i != 1 and i != 3:
            apply_player_action(game, i, PLAYER2)

    apply_player_action(game, 0, PLAYER1)
    apply_player_action(game, 2, PLAYER1)
    apply_player_action(game, 3, PLAYER1)
    apply_player_action(game, 4, PLAYER2)
    apply_player_action(game, 3, PLAYER2)
    apply_player_action(game, 4, PLAYER1)

    score = heuristic(game)
    assert score == 0


def test_heuristic_diagonal_expectScore200():
    game_string = "|==============|" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|      O X     |" \
                  "|    O X X     |" \
                  "|  O X X X O O |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"
    board = string_to_board(game_string)

    score = heuristic(board)

    assert score == 200
