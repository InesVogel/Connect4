from agents.agent_minimax import generate_alpha_beta
from agents.common import PLAYER1, PLAYER2, string_to_board


def test_minimax_firstAction_expectColumn3():
    game_string = "" \
                  "|==============|" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"
    board = string_to_board(game_string)

    best_action, saved_state = generate_alpha_beta(board, PLAYER1)

    assert best_action == 3


def test_minimax_forceMove_expectColumn3or5():
    # PLAYER1 will loose but still has to make a move
    game_string = "" \
                  "|==============|" \
                  "|              |" \
                  "|  X           |" \
                  "|O O O         |" \
                  "|X X O O       |" \
                  "|O X X X O     |" \
                  "|X X O X O     |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"
    board = string_to_board(game_string)

    best_action, saved_state = generate_alpha_beta(board, PLAYER1)

    assert best_action != None
    assert best_action in {3, 5}


def test_minimax_forceMove_expectColumn4or5():
    # PLAYER1 will loose but still has to make a move
    game_string = "|==============|" \
                  "|              |" \
                  "|              |" \
                  "|X   X         |" \
                  "|O X X         |" \
                  "|X O O O       |" \
                  "|X X O O O     |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"

    board = string_to_board(game_string)

    best_action, saved_state = generate_alpha_beta(board, PLAYER1)

    assert best_action != None
    assert best_action in {4, 5}


def test_minimax_block3Connect_expectColumn4():
    # PLAYER1 will loose but still has to make a move
    game_string = "|==============|" \
                  "|              |" \
                  "|              |" \
                  "|X             |" \
                  "|O     O O     |" \
                  "|X   X X O     |" \
                  "|X   O X O     |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"
    board = string_to_board(game_string)

    best_action, saved_state = generate_alpha_beta(board, PLAYER1)

    assert best_action == 4


def test_minimax_chooseWinOverBlocking_expectColumn1():
    # PLAYER1 will loose but still has to make a move
    game_string = "|==============|" \
                  "|              |" \
                  "|              |" \
                  "|X             |" \
                  "|O     O O     |" \
                  "|X   X X O     |" \
                  "|X O O X O     |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"
    board = string_to_board(game_string)

    best_action, saved_state = generate_alpha_beta(board, PLAYER1)

    assert best_action == 1


def test_minimax_chooseBlockingOverWin_expectColumn6():
    # PLAYER1 will loose but still has to make a move
    game_string = "|==============|" \
                  "|              |" \
                  "|              |" \
                  "|X             |" \
                  "|O           O |" \
                  "|X   X   X X O |" \
                  "|X   O   X O O |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"
    board = string_to_board(game_string)

    best_action, saved_state = generate_alpha_beta(board, PLAYER1)

    assert best_action == 6


def test_minimax_block3Connect_expectColumn5():
    game_string = "|==============|" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|X             |" \
                  "|X   X O O   O |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"
    board = string_to_board(game_string)
    best_action, saved_state = generate_alpha_beta(board, PLAYER1)

    assert best_action == 5


def test_minimax_block3Connect_expectColumn3():
    game_string = "|==============|" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|            O |" \
                  "|      X     O |" \
                  "|    X X     O |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"

    board = string_to_board(game_string)
    best_action, saved_state = generate_alpha_beta(board, PLAYER1)

    assert best_action == 6


def test_minimax_WIN_expectColumn4():
    game_string = "|==============|" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|  O           |" \
                  "|O X X X       |" \
                  "|X X O X O O O |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"
    board = string_to_board(game_string)
    best_action, saved_state = generate_alpha_beta(board, PLAYER1)

    assert best_action == 4


def test_minimax_anyMoveButColumn5():
    game_string = "|==============|" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|    O X X   X |" \
                  "|  O X X O   O |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"
    board = string_to_board(game_string)

    best_action, saved_state = generate_alpha_beta(board, PLAYER2)

    assert best_action in {0, 1, 2, 3, 4, 6}
    assert best_action != 5


def test_minimax_anyMoveButColumn4():
    game_string = "|==============|" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|      O       |" \
                  "|    O X X     |" \
                  "|  O X X X O O |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"
    board = string_to_board(game_string)

    best_action, saved_state = generate_alpha_beta(board, PLAYER1)

    assert best_action in {0, 1, 2, 3, 5, 6}
    assert best_action != 4


def test_minimax_win_bothPlayers():
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

    best_action, saved_state = generate_alpha_beta(board, PLAYER1)
    assert best_action == 4

    best_action, saved_state = generate_alpha_beta(board, PLAYER2)
    assert best_action == 4


def test_minimax_anyMoveButColumn3():
    game_string = "|==============|" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|              |" \
                  "|      O       |" \
                  "|      X X O   |" \
                  "|==============|" \
                  "|0 1 2 3 4 5 6 |"
    board = string_to_board(game_string)

    best_action, saved_state = generate_alpha_beta(board, PLAYER1)

    assert best_action in {0, 1, 2, 4, 5, 6}
    assert best_action != 3
