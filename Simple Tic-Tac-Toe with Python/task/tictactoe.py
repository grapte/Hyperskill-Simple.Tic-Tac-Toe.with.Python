# write your code here

board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


# user_in = input()
# board = [[], [], []]
# if set(user_in) <= {'X', 'O', '_'}:
#     for i in range(3):
#         for j in range(3):
#             board[i].append(user_in[i*3+j])
# else:
#     raise AssertionError("Invalid input")


def print_board():
    print("---------")
    for row in board:
        print("| ", end="")
        for col in row:
            print(f"{col} ", end="")
        print("|")
    print("---------")


def win(s):
    return (
            any(board[i] == [s, s, s] for i in range(3)) or
            any(all(board[j][i] == s for j in range(3)) for i in range(3)) or
            all(board[i][i] == s for i in range(3)) or
            all(board[i][2 - i] == s for i in range(3))
    )


print_board()
turn = 'X'

while True:
    while True:
        try:
            y, x = input().split()
            y, x = int(y), int(x)
        except ValueError:
            print("You should enter numbers!")
            continue
        if not (0 < y < 4) or not (0 < x < 4):
            print("Coordinates should be from 1 to 3!")
            continue
        if board[y - 1][x - 1] != '_':
            print("This cell is occupied! Choose another one!")
            continue

        board[y - 1][x - 1] = turn
        break

    turn = 'O' if turn == 'X' else 'X'

    count = {"X": 0, "O": 0, "_": 0}
    for i in range(3):
        for j in range(3):
            count[board[i][j]] += 1

    x_win = win('X')
    o_win = win('O')
    is_not_finished = not x_win and not o_win and count['_'] > 0
    is_impossible = abs(count['X'] - count['O']) > 1 or (x_win and o_win)
    is_draw = not x_win and not o_win and count['_'] == 0

    print_board()
    if is_impossible:
        print("Impossible")
        raise AssertionError("impossible board")
    else:
        if is_not_finished:
            continue
            # print("Game not finished")
        elif is_draw:
            print("Draw")
            break
        elif x_win:
            print("X wins")
            break
        elif o_win:
            print("O wins")
            break
        else:
            raise AssertionError("unreachable")
