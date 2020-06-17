vars = dict()
vars['//'] = "'"
ascii_letters = 'abcdefghijklmnopqrstuvwxyz'


def has_ascii(name):
    return any(map(lambda c: c in ascii_letters, name))


def validate(name):
    return all(map(lambda c: c in ascii_letters, name))


def replace_vars(old):
    new = old
    for i, j in vars.items():
        new = new.replace(i, j)
    return new    


while True:
    cmd = input().replace(' ', '')
    if cmd == '/exit':
        print('Bye!')
        break
    elif cmd == '/help':
        print('The program calculates the sum of numbers')
        continue
    elif cmd == '':
        continue
    elif cmd[0] == '/':
        print('Unknown command')
        continue
        
    equal = cmd.split('=')
    if len(equal) == 2:
        left, right = equal
        if validate(left):
            try:
                vars[left] = str(eval(replace_vars(right)))
            except:
                print('Invalid assignment')    
        else:
            print('Invalid identifier')  
    elif len(equal) > 2:
        print('Invalid assignment')  
    else:
        try:
            r = replace_vars(cmd)
            if has_ascii(r):
                print('Unknown variable')
                continue
            print(int(eval(r)))
        except:
            print('Invalid expression')
