import numpy as np

from agents.common import PLAYER1, PLAYER2, NO_PLAYER, count_occupied_fields, WindowSize


def test_count_occupied_fields_PLAYER1_expectCount1():
    window1 = np.array([NO_PLAYER, NO_PLAYER, NO_PLAYER, PLAYER1])
    window2 = np.array([PLAYER1, NO_PLAYER, NO_PLAYER, NO_PLAYER])
    window3 = np.array([NO_PLAYER, PLAYER1, NO_PLAYER, NO_PLAYER])
    window4 = np.array([NO_PLAYER, NO_PLAYER, PLAYER1, NO_PLAYER])
    expect_count = 1

    windows = [window1, window2, window3, window4]

    for window in windows:
        assert count_occupied_fields(window, PLAYER1) == expect_count
        assert count_occupied_fields(window, PLAYER2) == 0
        assert count_occupied_fields(window, NO_PLAYER) == WindowSize - expect_count


def test_count_occupied_fields_PLAYER2_expectCount1():
    window1 = np.array([NO_PLAYER, NO_PLAYER, NO_PLAYER, PLAYER2])
    window2 = np.array([PLAYER2, NO_PLAYER, NO_PLAYER, NO_PLAYER])
    window3 = np.array([NO_PLAYER, PLAYER2, NO_PLAYER, NO_PLAYER])
    window4 = np.array([NO_PLAYER, NO_PLAYER, PLAYER2, NO_PLAYER])
    expect_count = 1

    windows = [window1, window2, window3, window4]

    for window in windows:
        assert count_occupied_fields(window, PLAYER1) == 0
        assert count_occupied_fields(window, PLAYER2) == expect_count
        assert count_occupied_fields(window, NO_PLAYER) == WindowSize - expect_count


def test_count_occupied_fields_PLAYER1_expectCount2():
    window1 = np.array([NO_PLAYER, NO_PLAYER, PLAYER1, PLAYER1])
    window2 = np.array([PLAYER1, NO_PLAYER, NO_PLAYER, PLAYER1])
    window3 = np.array([PLAYER1, PLAYER1, NO_PLAYER, NO_PLAYER])
    expect_count = 2

    windows = [window1, window2, window3]

    for window in windows:
        assert count_occupied_fields(window, PLAYER1) == expect_count
        assert count_occupied_fields(window, PLAYER2) == 0
        assert count_occupied_fields(window, NO_PLAYER) == WindowSize - expect_count


def test_count_occupied_fields_PLAYER2_expectCount2():
    window1 = np.array([NO_PLAYER, NO_PLAYER, PLAYER2, PLAYER2])
    window2 = np.array([PLAYER2, NO_PLAYER, NO_PLAYER, PLAYER2])
    window3 = np.array([PLAYER2, PLAYER2, NO_PLAYER, NO_PLAYER])
    expect_count = 2

    windows = [window1, window2, window3]

    for window in windows:
        assert count_occupied_fields(window, PLAYER1) == 0
        assert count_occupied_fields(window, PLAYER2) == expect_count
        assert count_occupied_fields(window, NO_PLAYER) == WindowSize - expect_count


def test_count_occupied_fields_PLAYER1_expectCount3():
    window1 = np.array([NO_PLAYER, PLAYER1, PLAYER1, PLAYER1])
    window2 = np.array([PLAYER1, NO_PLAYER, PLAYER1, PLAYER1])
    window3 = np.array([PLAYER1, PLAYER1, NO_PLAYER, PLAYER1])
    window4 = np.array([PLAYER1, PLAYER1, PLAYER1, NO_PLAYER])
    expect_count = 3

    windows = [window1, window2, window3, window4]

    for window in windows:
        assert count_occupied_fields(window, PLAYER1) == expect_count
        assert count_occupied_fields(window, PLAYER2) == 0
        assert count_occupied_fields(window, NO_PLAYER) == WindowSize - expect_count


def test_count_occupied_fields_PLAYER2_expectCount3():
    window1 = np.array([NO_PLAYER, PLAYER2, PLAYER2, PLAYER2])
    window2 = np.array([PLAYER2, NO_PLAYER, PLAYER2, PLAYER2])
    window3 = np.array([PLAYER2, PLAYER2, NO_PLAYER, PLAYER2])
    window4 = np.array([PLAYER2, PLAYER2, PLAYER2, NO_PLAYER])
    expect_count = 3

    windows = [window1, window2, window3, window4]

    for window in windows:
        assert count_occupied_fields(window, PLAYER1) == 0
        assert count_occupied_fields(window, PLAYER2) == expect_count
        assert count_occupied_fields(window, NO_PLAYER) == WindowSize - expect_count


def test_count_occupied_fields_PLAYER1_expectCount4():
    window1 = np.array([PLAYER1, PLAYER1, PLAYER1, PLAYER1])

    expect_count = 4

    windows = [window1]

    for window in windows:
        assert count_occupied_fields(window, PLAYER1) == expect_count
        assert count_occupied_fields(window, PLAYER2) == 0
        assert count_occupied_fields(window, NO_PLAYER) == WindowSize - expect_count


def test_count_occupied_fields_PLAYER2_expectCount4():
    window1 = np.array([PLAYER2, PLAYER2, PLAYER2, PLAYER2])

    expect_count = 4

    windows = [window1]

    for window in windows:
        assert count_occupied_fields(window, PLAYER1) == 0
        assert count_occupied_fields(window, PLAYER2) == expect_count
        assert count_occupied_fields(window, NO_PLAYER) == WindowSize - expect_count


def test_count_occupied_fields_mixedPlayer1_expectCount2():
    window1 = np.array([PLAYER2, PLAYER2, PLAYER1, PLAYER1])
    window2 = np.array([PLAYER1, PLAYER2, PLAYER2, PLAYER1])
    window3 = np.array([PLAYER1, PLAYER1, PLAYER2, PLAYER2])
    expect_count = 2

    windows = [window1, window2, window3]

    for window in windows:
        assert count_occupied_fields(window, PLAYER1) == expect_count
        assert count_occupied_fields(window, PLAYER2) == WindowSize - expect_count
        assert count_occupied_fields(window, NO_PLAYER) == 0


def test_count_occupied_fields_mixedlayer2_expectCount2():
    window1 = np.array([PLAYER1, PLAYER1, PLAYER2, PLAYER2])
    window2 = np.array([PLAYER2, PLAYER1, PLAYER1, PLAYER2])
    window3 = np.array([PLAYER2, PLAYER2, PLAYER1, PLAYER1])
    expect_count = 2

    windows = [window1, window2, window3]

    for window in windows:
        assert count_occupied_fields(window, PLAYER1) == WindowSize - expect_count
        assert count_occupied_fields(window, PLAYER2) == expect_count
        assert count_occupied_fields(window, NO_PLAYER) == 0


def test_count_occupied_fields_mixedPlayer1_expectCount3():
    window1 = np.array([PLAYER2, PLAYER1, PLAYER1, PLAYER1])
    window2 = np.array([PLAYER1, PLAYER2, PLAYER1, PLAYER1])
    window3 = np.array([PLAYER1, PLAYER1, PLAYER2, PLAYER1])
    window4 = np.array([PLAYER1, PLAYER1, PLAYER1, PLAYER2])
    expect_count = 3

    windows = [window1, window2, window3, window4]

    for window in windows:
        assert count_occupied_fields(window, PLAYER1) == expect_count
        assert count_occupied_fields(window, PLAYER2) == WindowSize - expect_count
        assert count_occupied_fields(window, NO_PLAYER) == 0


def test_count_occupied_fields_mixedPlayer2_expectCount3():
    window1 = np.array([PLAYER1, PLAYER2, PLAYER2, PLAYER2])
    window2 = np.array([PLAYER2, PLAYER1, PLAYER2, PLAYER2])
    window3 = np.array([PLAYER2, PLAYER2, PLAYER1, PLAYER2])
    window4 = np.array([PLAYER2, PLAYER2, PLAYER2, PLAYER1])
    expect_count = 3

    windows = [window1, window2, window3, window4]

    for window in windows:
        assert count_occupied_fields(window, PLAYER1) == WindowSize - expect_count
        assert count_occupied_fields(window, PLAYER2) == expect_count
        assert count_occupied_fields(window, NO_PLAYER) == 0
