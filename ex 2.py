import math

class Tmoney:
    def __init__(self,dollar_exchange_rate,money):
        self.dollar_exchange_rate = dollar_exchange_rate
        self.money_in_dollars = money

    @property
    def money_in_dollars(self):
        return self.__money
    @money_in_dollars.setter
    def money_in_dollars(self,a):
        self.__money = a

    def add_to_money(self, money_in_uah):
        x = math.ceil(money_in_uah/self.dollar_exchange_rate*100)/100
        self.money_in_dollars += x
    def sub_money(self, money_in_uah):
        x = math.ceil(money_in_uah / self.dollar_exchange_rate * 100) / 100
        self.money_in_dollars -= x

    def convert_to_uah(self):
        return self.money_in_dollars *100
t = Tmoney(27,2000)
t.add_to_money(253)
print(t.money_in_dollars,"$")
print(t.convert_to_uah(),"₴")
