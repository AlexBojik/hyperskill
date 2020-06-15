lst = list('_________')


def print_matrix():
    print('---------')
    print('| {0} {1} {2} |'.format(lst[0], lst[1], lst[2]))
    print('| {0} {1} {2} |'.format(lst[3], lst[4], lst[5]))
    print('| {0} {1} {2} |'.format(lst[6], lst[7], lst[8]))
    print('---------')


def is_win(i, j, k):
    return lst[i] if lst[i] == lst[j] == lst[k] else ''


def count(sym):
    return len([i for i in lst if i == sym])


print_matrix()
current_sym = 'X'
while True:
    try:
        x_str, y_str = input('Enter the coordinates:').split(' ')

        x = int(x_str)
        y = int(y_str)
        if x in (1, 2, 3) and y in (1, 2, 3):
            ind = x - 3 * y + 8
            if lst[ind] in ('X', 'O'):
                print('This cell is occupied! Choose another one!')
            else:
                lst[ind] = current_sym
                current_sym = 'X' if current_sym == 'O' else 'O'
                print_matrix()
                win = is_win(0, 1, 2) + is_win(3, 4, 5) + is_win(6, 7, 8) + is_win(2, 4, 6) \
                    + is_win(0, 3, 6) + is_win(1, 4, 7) + is_win(2, 5, 8) + is_win(0, 4, 8)
                if win == 'O':
                    print('O wins')
                    break
                elif win == 'X':
                    print('X wins')
                    break
                else:
                    if count('_') == 0:
                        print('Draw')
                        break
        else:
            print('Coordinates should be from 1 to 3!')
    except TypeError:
        print('You should enter numbers!')
