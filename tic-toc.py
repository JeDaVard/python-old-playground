def render_board(board):
    for idx, row in enumerate(board):
        visual_row = ''
        for col_idx, col in enumerate(row):
            visual_row += col+' | ' if col_idx != len(row)-1 else col
        print(visual_row)
        if idx != len(board)-1:
            print('––  ' * len(row))


def choose_player():
    first = input('Please, enter chose your mark \n').upper()

    while first != 'O' and first != 'X':
        first = input('Please, enter O or X \n').upper()
    second = 'O' if first == 'X' else 'X'

    return first, second


def init(board):
    (f, s) = choose_player()
    print(f'\nPlayer 1: {f}')
    print(f'Player 2: {s} \n')
    render_board(board)
    return f


def check_winner(row):
    x = all('X' == each for each in row)
    o = all('O' == each for each in row)
    if x:
        return 'X'
    if o:
        return 'O'
    return None


def check_result(board):
    for row in board:
        winner = check_winner(row)
        if winner:
            return winner

    for col in range(len(board[0])):
        new_row = [row[col] for row in board]

        winner = check_winner(new_row)
        if winner:
            return winner

    new_row = []
    for row in range(len(board)):
        new_row.append(board[row][row])
    winner = check_winner(new_row)
    if winner:
        return winner

    new_row = []
    for row in range(len(board)):
        new_row.append(board[len(board)-1-row][row])
    winner = check_winner(new_row)
    if winner:
        return winner


def mark(board, marker, **kwargs):
    is_marked = board[kwargs['y']][kwargs['x']] != ' '
    if is_marked:
        return False
    board[kwargs['y']][kwargs['x']] = marker
    return True


def play(col, row):
    board = [[' ' for i in range(col)] for i in range(row)]
    player = init(board)

    winner = None

    while not winner:
        x = int(input('Column number:\n'))-1
        y = int(input('Row number:\n'))-1
        mark_res = mark(board, player, x=x, y=y)
        if mark_res:
            winner = check_result(board)
            player = 'X' if player == 'O' else 'O'
            render_board(board)
        else:
            print('No no no. You can\'t mark that, it\'s already marked')
            render_board(board)

    print(f'CONGRATS, {winner.upper()}, you won!!!')
    return winner


play(3, 3)
