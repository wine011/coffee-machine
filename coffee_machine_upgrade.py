class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.d_cups = 9
        self.money = 550
        self.action = None
        self.coffee_type = None

    def main(self, action):
        while True:
            # Choose action
            action = input("Write action (buy, fill, take, remaining, exit):\n")

            self.action = action

            if self.action == 'buy':
                self.buy()
            elif self.action == 'fill':
                self.fill()
            elif self.action == 'take':
                self.take()
            elif self.action == 'remaining':
                self.remaining()
            elif self.action == 'exit':
                break
    
    def buy(self, coffee_type=None):
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
        self.coffee_type = coffee_type

        if self.coffee_type == '1':
            # 250 ml of water and 16 g of coffee beans. It costs $4.
            if self.water >= 250 and self.coffee_beans >= 16:
                self.water = self.water - 250
                self.coffee_beans = self.coffee_beans - 16
                self.d_cups = self.d_cups - 1
                self.money = self.money + 4
                print("I have enough resources, making you a coffee!")
            else:
                if self.water < 250:
                    print("Sorry, not enough water!")
                elif self.coffee_beans < 16:
                    print("Sorry, not enough coffee beans!")
                elif self.d_cups < 1:
                    print("Sorry, not enough cups!")
            return  self.water, self.coffee_beans, self.d_cups, self.money
            
        elif self.coffee_type == '2':
            # 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
            if self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20:
                self.water = self.water - 350
                self.milk = self.milk - 75
                self.coffee_beans = self.coffee_beans - 20
                self.d_cups = self.d_cups - 1
                self.money = self.money + 7
                print("I have enough resources, making you a coffee!")
            else:
                if self.water < 350:
                    print("Sorry, not enough water!")
                elif self.milk < 75:
                    print("Sorry, not enough milk!")
                elif self.coffee_beans < 20:
                    print("Sorry, not enough coffee beans!")
                elif self.d_cups < 1:
                    print("Sorry, not enough cups!")
            return self.water, self.coffee_beans, self.milk, self.d_cups, self.money

        elif self.coffee_type == '3':
            # 200 ml of water, 100 ml of milk, and 12 g of coffee beans. It costs $6.
            
            if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12:
                self.water = self.water - 200
                self.milk = self.milk - 100
                self.coffee_beans = self.coffee_beans - 12
                self.d_cups = self.d_cups - 1
                self.money = self.money + 6
                print("I have enough resources, making you a coffee!")
            else:
                if self.water < 200:
                    print("Sorry, not enough water!")
                elif self.milk < 100:
                    print("Sorry, not enough milk!")
                elif self.coffee_beans < 12:
                    print("Sorry, not enough coffee beans!")
                elif self.d_cups < 1:
                    print("Sorry, not enough cups!")
            return self.water, self.coffee_beans, self.milk, self.d_cups, self.money

    def fill(self, add_water=None, add_milk=None, add_coffee_beans=None, add_d_cups=None):
        add_water = int(input("Write how many ml of water you want to add:\n"))
        add_milk = int(input("Write how many ml of milk you want to add:\n"))
        add_coffee_beans = int(input("Write how many grams of coffee beans you want to add:\n"))
        add_d_cups = int(input("Write how many disposable cups you want to add:\n"))

        self.water = self.water + add_water
        self.milk = self.milk + add_milk
        self.coffee_beans = self.coffee_beans + add_coffee_beans
        self.d_cups = self.d_cups + add_d_cups
        self.money = self.money
        return self.water, self.milk, self.coffee_beans, self.d_cups, self.money

    def take(self):
        print(f"I gave you {self.money}")
        self.money -= self.money
        return self.money
    
    # When user types 'remaining', the output shows all available resources
    def remaining(self):
        print("The coffee machine has:")
        print(f"""{self.water} ml of water
{self.milk} ml of milk
{self.coffee_beans} g of coffee beans
{self.d_cups} disposable cups
${self.money} of money""")


coffee = CoffeeMachine()
coffee.main(None)