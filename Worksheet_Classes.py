import math

class RegularPolygon:
    def __init__(self, n=3, side=1, x=0, y=0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def get_perimeter(self):
        return self.__n * self.__side

    def get_area(self):
        return (self.__n * (self.__side ** 2)) / (4 * math.tan(math.pi / self.__n))
def main():
    polygon1 = RegularPolygon()
    polygon2 = RegularPolygon(6, 4)
    polygon3 = RegularPolygon(10, 4, 5.6, 7.8)
    print(f"Polygon 1 - Perimeter: {polygon1.get_perimeter()}, Area: {polygon1.get_area()}")
    print(f"Polygon 2 - Perimeter: {polygon2.get_perimeter()}, Area: {polygon2.get_area()}")
    print(f"Polygon 3 - Perimeter: {polygon3.get_perimeter()}, Area: {polygon3.get_area()}")
main()

class Stock:
    def __init__(self, symbol, name, previous_closing_price, current_price):
        self.__symbol = symbol
        self.__name = name
        self.__previous_closing_price = previous_closing_price
        self.__current_price = current_price

    def get_symbol(self):
        return self.__symbol

    def get_name(self):
        return self.__name

    def get_previous_closing_price(self):
        return self.__previous_closing_price

    def get_current_price(self):
        return self.__current_price

    def get_change_percent(self):
        change_percent = ((self.__current_price - self.__previous_closing_price) / self.__previous_closing_price) * 100
        return change_percent

stock = Stock("NVDA", "Nvidia Inc.", 488.00, 492.00)
print("Stock Name:", stock.get_name())
print("Stock Symbol:", stock.get_symbol())
print("Previous Closing Price:", stock.get_previous_closing_price())
print("Current Price:", stock.get_current_price())
print("Change Percent:", round(stock.get_change_percent(), 2), "%")

class Account:
    def __init__(self, id=0, balance=100, annual_interest_rate=0):
        self.__id = id
        self.__balance = balance
        self.__annual_interest_rate = annual_interest_rate

    def get_monthly_interest_rate(self):
        return self.__annual_interest_rate / 12 / 100

    def get_monthly_interest(self):
        monthly_interest_rate = self.get_monthly_interest_rate()
        return self.__balance * monthly_interest_rate

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    # Getters for id and balance
    def get_id(self):
        return self.__id

    def get_balance(self):
        return self.__balance

def main():
    account = Account(id=1122, balance=20000, annual_interest_rate=4.5)
    account.withdraw(2500)
    account.deposit(3000)
    print(f"Account ID: {account.get_id()}")
    print(f"Balance: ${account.get_balance():,.2f}")
    print(f"Monthly Interest Rate: {account.get_monthly_interest_rate() * 100:.2f}%")
    print(f"Monthly Interest: ${account.get_monthly_interest():,.2f}")
main()
