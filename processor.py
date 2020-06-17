def input_matrix(number = ''):
    mess = 'Enter matrix size: '
    mess1 = 'Enter matrix: '
    if number != '':
        mess = f'Enter size of {number} matrix: '
        mess1 = f'Enter {number} matrix: '
    x, y = [int(i) for i in input(mess).split()]
    print(mess1)
    matrix = list()
    for _ in range(x):
        matrix.append([float(i) for i in input().split()])
    return x, y, matrix


def print_menu():
    print('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')


def print_transpose_menu():
    print('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')


def print_result(matrix):
    print('The result is:')
    for line in matrix:
        print(line)
    print()


def print_error():
    print('The operation cannot be performed.')


def add():
    x1, y1, a = input_matrix('first')
    x2, y2, b = input_matrix('second')
    res = list()
    if x1 == x2 and y1 == y2:
        for i in range(0, x1):
            line = ''
            for j in range(0, x2):
                line += str(a[i][j] + b[i][j]) + ' '
            res.append(line)
        print_result(res)
    else:
        print_error()


def multiply_constant():
    x1, y1, a = input_matrix('first')
    c = float(input('Enter constant:'))
    res = list()
    for i in range(0, x1):
        line = ''
        for j in range(0, y1):
            line += str(a[i][j] * c) + ' '
        res.append(line)
    print_result(res)


def multiply():
    x1, y1, a = input_matrix('first')
    x2, y2, b = input_matrix('second')
    res = list()
    if x2 == y1:
        t = 0
        for i in range(0, x1):
            s = ''
            for j in range(0, y2):
                t = 0
                for k in range(0, y1):
                    t += a[i][k] * b[k][j]
                s += str(t) + ' '
            res.append(s)
        print_result(res)
    else:
        print_error()


def transpose_main(m, x, y):
    res = list()
    for i in range(0, x):
        line = ''
        for j in range(0, y):
            line += str(m[j][i]) + ' '
        res.append(line)
    print_result(res)


def transpose_side(m, x, y):
    res = list()
    for i in reversed(range(0, x)):
        line = ''
        for j in reversed(range(0, y)):
            line += str(m[j][i]) + ' '
        res.append(line)
    print_result(res)


def transpose_vertical(m, x, y):
    res = list()
    for i in range(0, x):
        line = ''
        for j in reversed(range(0, y)):
            line += str(m[i][j]) + ' '
        res.append(line)
    print_result(res)


def transpose_horizontal(m, x, y):
    res = list()
    for i in reversed(range(0, x)):
        line = ''
        for j in range(0, y):
            line += str(m[i][j]) + ' '
        res.append(line)
    print_result(res)


def transpose():
    print_transpose_menu()
    t = input('Your choice:')
    x, y, matrix = input_matrix()
    if t == '1':
        transpose_main(matrix, x, y)
    elif t == '2':
        transpose_side(matrix, x, y)
    elif t == '3':
        transpose_vertical(matrix, x, y)
    elif t == '4':
        transpose_horizontal(matrix, x, y)


def cofactor(i, j, x, matrix):
    new = list()
    for k in range(x):
        if k == i:
            continue
        line = list()
        for m in range(x):
            if m == j:
                continue
            line.append(matrix[k][m])
        new.append(line)
    return ((-1) ** (i + j)) * calc_determinant(x - 1, new)


def calc_determinant(x, matrix):
    if x == 1:
        return matrix[0][0]
    if x == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for i in range(x):
        det += matrix[0][i] * cofactor(0, i, x, matrix)
    return det


def determinant():
    x, y, matrix = input_matrix()
    print('The result is:')
    print(calc_determinant(x, matrix))


def inverse():
    x, y, matrix = input_matrix()
    det = calc_determinant(x, matrix)

    if x != y or det == 0:
        print("This matrix doesn't have an inverse.")
    else:
        res = list()
        for i in range(x):
            line = ''
            for j in range(x):
                line += str(cofactor(j, i, x, matrix) / det) + ' '
            res.append(line)
        print_result(res)


while True:
    print_menu()
    s = input('Your choice:')
    if s == '0':
        break
    elif s == '1':
        add()
    elif s == '2':
        multiply_constant()
    elif s == '3':
        multiply()
    elif s == '4':
        transpose()
    elif s == '5':
        determinant()
    elif s == '6':
        inverse()
