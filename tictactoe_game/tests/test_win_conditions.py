from tictactoe_game.board import check_if_win, Point


def test_empty_board():
    board = 5 * [5 * [0]]
    assert not check_if_win(board, Point(0, 0), 5)


def test_win_horizontal_board_last_row():
    board = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
    ]
    assert check_if_win(board, Point(4, 4), 5)


def test_win_horizontal_board_first_row():
    board = [
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert check_if_win(board, Point(0, 0), 5)


def test_win_horizontal_board_middle_row():
    board = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert check_if_win(board, Point(2, 2), 5)


def test_win_horizontal_horizontal_long_false():
    board = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    assert not check_if_win(board, Point(2, 2), 5)


def test_win_horizontal_horizontal_long_true():
    board = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    assert check_if_win(board, Point(2, 2), 5)


def test_win_vertical_board_middle_row():
    board = [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert check_if_win(board, Point(4, 2), 5)


def test_win_vertical_board_first_col():
    board = [
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
    ]
    assert check_if_win(board, Point(0, 0), 5)


def test_win_vertical_board_last_col():
    board = [
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
    ]
    assert check_if_win(board, Point(2, 4), 5)


def test_win_vertical_horizontal_long_false():
    board = [
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
    ]
    assert not check_if_win(board, Point(2, 2), 5)


def test_win_vertical_horizontal_long_true():
    board = [
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
    ]
    assert check_if_win(board, Point(2, 2), 5)


def test_win_diagonal_right_up_board_middle_row():
    board = [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0],
    ]
    assert check_if_win(board, Point(0, 4), 5)


def test_win_diagonal_right_up_horizontal_long_false():
    board = [
        [0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0],
    ]
    assert not check_if_win(board, Point(1, 4), 5)


def test_win_diagonal_right_up_horizontal_long_true():
    board = [
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0],
    ]
    assert check_if_win(board, Point(1, 4), 5)


def test_win_diagonal_right_down_board_middle_row():
    board = [
        [1, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
    ]
    assert check_if_win(board, Point(4, 4), 5)


def test_win_diagonal_right_down_horizontal_long_false():
    board = [
        [1, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [1, 0, 1, 0, 0, 1],
    ]
    assert not check_if_win(board, Point(1, 1), 5)


def test_win_diagonal_right_down_horizontal_long_true():
    board = [
        [1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [1, 0, 1, 0, 0, 0],
    ]
    assert check_if_win(board, Point(1, 1), 5)
