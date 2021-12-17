from collections import namedtuple

Point = namedtuple('Point', 'row col')


# todo refactor it
def check_if_win(board, point, line_lenght):
    checks = [calculate_vertical_line,
              calculate_horizontal_line,
              calculate_diagonal_line_right_down,
              calculate_diagonal_line_right_up]

    for chech in checks:
        if chech(board, point, line_lenght):
            return True
    return False


def calculate_horizontal_line(board, point, line_lenght=5):
    length = 1
    for col in range(point.col + 1, len(board[0])):
        if board[point.row][col] == 1:
            length += 1
            if length >= line_lenght:
                return True
        else:
            break
    for col in range(point.col - 1, -1, -1):
        if board[point.row][col] == 1:
            length += 1
            if length >= line_lenght:
                return True
        else:
            break
    return False


def calculate_vertical_line(board, point, line_lenght=5):
    length = 1
    for row in range(point.row + 1, len(board)):
        if board[row][point.col] == 1:
            length += 1
            if length >= 5:
                return True
        else:
            break
    for row in range(point.row - 1, -1, -1):
        if board[row][point.col] == 1:
            length += 1
            if length >= line_lenght:
                return True
        else:
            break
    return False


def calculate_diagonal_line_right_up(board, point, line_lenght=5):
    length = 1
    for row, col in zip(range(point.row - 1, -1, -1), range(point.col + 1, len(board))):
        if board[row][col] == 1:
            length += 1
            if length >= line_lenght:
                return True
        else:
            break
    for row, col in zip(range(point.row + 1, len(board)), range(point.col - 1, -1, -1)):
        if board[row][col] == 1:
            length += 1
            if length >= line_lenght:
                return True
        else:
            break
    return False


def calculate_diagonal_line_right_down(board, point, line_lenght=5):
    length = 1
    for row, col in zip(range(point.row + 1, len(board)), range(point.col + 1, len(board))):
        if board[row][col] == 1:
            length += 1
            if length >= line_lenght:
                return True
        else:
            break
    for row, col in zip(range(point.row - 1, -1, -1), range(point.col - 1, -1, -1)):
        if board[row][col] == 1:
            length += 1
            if length >= line_lenght:
                return True
        else:
            break
    return False
