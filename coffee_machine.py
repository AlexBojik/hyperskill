class CoffeeMachine:
    def __init__(self, water, milk, coffee, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.disposable_cups = disposable_cups
        self.money = money
        self.state = 'wait'
        self.fill_kind = 0
        print('Write action (buy, fill, take, remaining, exit):')

    def processing(self, cmd):
        if self.state == 'wait':
            if cmd == 'buy':
                self.state = 'buy'
                print()
                print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            if cmd == 'fill':
                self.state = 'fill'
                print()
                print('Write how many ml of water do you want to add:')
            if cmd == 'remaining':
                self.print_info()
                print()
                print('Write action (buy, fill, take, remaining, exit):')
            elif cmd == 'take':
                print(f'I gave you ${self.money}')
                self.money = 0
                print()
                print('Write action (buy, fill, take, remaining, exit):')
            else:
                self.state = cmd
        elif self.state == 'buy':
            self.buy(cmd)
        elif self.state == 'fill':
            self.fill(cmd)

    def buy(self, cmd):
        if cmd == '1':
            self.make_coffee(250, 0, 16, 4)
        elif cmd == '2':
            self.make_coffee(350, 75, 20, 7)
        elif cmd == '3':
            self.make_coffee(200, 100, 12, 6)
        self.state = 'wait'
        print()
        print('Write action (buy, fill, take, remaining, exit):')

    def fill(self, cmd):
        if self.fill_kind == 0:
            self.water += int(cmd)
            self.fill_kind += 1
            print('Write how many ml of milk do you want to add:')
        elif self.fill_kind == 1:
            self.milk += int(cmd)
            self.fill_kind += 1
            print('Write how many grams of coffee beans do you want to add:')
        elif self.fill_kind == 2:
            self.coffee += int(cmd)
            self.fill_kind += 1
            print('Write how many disposable cups of coffee do you want to add:')
        elif self.fill_kind == 3:
            self.fill_kind += 1
            print()
            print('Write action (buy, fill, take, remaining, exit):')
            self.state = 'wait'
            self.disposable_cups += int(cmd)
            self.fill_kind = 0

    def make_coffee(self, w, m, c, mon):
        if self.water < w:
            print('Sorry, not enough water!')
        elif self.milk < m:
            print('Sorry, not enough milk!')
        elif self.coffee < c:
            print('Sorry, not enough coffee beans!')
        elif self.disposable_cups < 1:
            print('Sorry, not enough disposable cups!')
        else:
            self.water -= w
            self.milk -= m
            self.coffee -= c
            self.disposable_cups -= 1
            self.money += mon
            print('I have enough resources, making you a coffee!')

    def print_info(self):
        print()
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee} of coffee beans')
        print(f'{self.disposable_cups} of disposable cups')
        print(f'${self.money} of money')


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
while coffee_machine.state != 'exit':
    coffee_machine.processing(input())
