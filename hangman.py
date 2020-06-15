from random import choice
print('H A N G M A N')
list_ = ['python', 'java', 'kotlin', 'javascript']
opt = choice(list_)
t = '-'*(len(opt))
ins = set()
n = 0
start = False

while True:
    if not start:
        s = input('Type "play" to play the game, "exit" to quit:')
        if s == 'play':
            ins.clear()
            opt = choice(list_)
            t = '-'*(len(opt))
            n = 0
            start = True
            print()
            print(t)
        elif s == 'exit':
            break
    else:
        s = input('Input a letter:')
        if len(s) > 1:
            print('You should input a single letter')
        elif s not in 'abcdefghijklmnopqrstuvwxyz':
            print('It is not an ASCII lowercase letter')
        elif s in ins:
            print('You already typed this letter')
        elif s not in opt:
            n += 1
            print('No such letter in the word')
        ins.add(s)
        if n == 8:
            start = False
            print('You are hanged!')
            print()
            continue
        t = ''
        for i in opt:
            if i in ins:
                t += i
            else:
                t += '-'
        print()
        print(t)
        if t in opt:
            start = False
            print('You guessed the word!')
            print('You survived!') 
            print()
