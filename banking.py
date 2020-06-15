import random as rnd
import sqlite3 as sql


def luhn_check(number):
    luhn = 0
    for num, i in enumerate(number):
        x = int(i)
        if num % 2 == 0:
            x = x * 2
        if x > 9:
            x = x - 9
        luhn += x
    last = str((10 - luhn % 10) % 10)
    return last


def generate_card_number():
    rand9 = str(rnd.randint(111111111, 999999999))
    card_number = '400000' + rand9

    return card_number + luhn_check(card_number)


class Card:
    cards = dict()
    current = None

    def __init__(self):
        self.number = generate_card_number()
        self.pin = str(rnd.randint(1111, 9999))
        self.balance = 0
        Card.cards[self.number] = self.pin


def create_account():
    print('Your card has been created')
    card = Card()
    cur = conn.cursor()
    cur.execute("insert into card(id, number, pin) values(?, ?, ?)", (rnd.randint(1, 1000000), card.number, card.pin))
    conn.commit()
    print('Your card number:')
    print(card.number)
    print('Your card PIN:')
    print(card.pin)


def log_in():
    print('Enter your card number:')
    number = input()
    print('Enter your PIN:')
    pin = input()

    cur = conn.cursor()
    cur.execute("select balance, id, number from card where number = ? and pin = ?", (number, pin))
    row = cur.fetchone()
    if row is not None:
        print('You have successfully logged in!')
        Card.current = row
    else:
        print('Wrong card number or PIN!')


def start():
    if Card.current is None:
        print('1. Create an account')
        print('2. Log into account')
        print('0. Exit')
    else:
        print('1. Balance')
        print('2. Add income')
        print('3. Do transfer')
        print('4. Close account')
        print('5. Log out')
        print('0. Exit')

    return input()


def add_income():
    print('Enter income:')
    i = int(input())
    Card.current = (Card.current[0] + i, Card.current[1], Card.current[2])
    cur = conn.cursor()
    cur.execute("update card set balance = ? where id = ?", (Card.current[0], Card.current[1]))
    conn.commit()


def do_transfer():
    print('Enter card number:')
    c = input()
    if c == Card.current[2]:
        print("You can't transfer money to the same account!")
        return
    if luhn_check(c[:-1]) != c[-1]:
        print("Probably you made mistake in card number. Please try again!")
        return

    cur = conn.cursor()
    cur.execute("select balance from card where number = ?", (c, ))
    row = cur.fetchone()
    if row is None:
        print("Such a card does not exist.")
        return

    print('Enter how much money you want to transfer:')
    i = int(input())
    if Card.current[0] < i:
        print("Not enough money!")
        return
    Card.current = (Card.current[0] - i, Card.current[1], Card.current[2])

    cur.execute("update card set balance = ? where id = ?", (Card.current[0], Card.current[1]))
    cur.execute("update card set balance = balance + ? where number = ?", (i, c))
    conn.commit()
    print('Success')


def close_account():
    cur = conn.cursor()
    cur.execute("delete from card where id = ?", (Card.current[1], ))
    conn.commit()
    Card.current = None


conn = sql.connect('card.s3db')
conn.execute('create table if not exists card(id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)')
conn.commit()

c = conn.cursor()
c.execute('select * from card')
rows = c.fetchall()
for r in rows:
    print(r)

while True:
    cmd = start()
    print()
    if cmd == '0':
        print('Bye!')
        break
    elif Card.current is None:
        if cmd == '1':
            create_account()
        else:
            log_in()
    else:
        if cmd == '1':
            print('Balance: {}'.format(Card.current[0]))
        elif cmd == '2':
            add_income()
        elif cmd == '3':
            do_transfer()
        elif cmd == '4':
            close_account()
        else:
            Card.current = None
    print()
conn.close()
