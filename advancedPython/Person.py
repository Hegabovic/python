class Person:

    def __init__(self, fullname="", money=0, sleep_mood="", health_rate=0):
        self.__full_name = fullname
        self.__money = money
        self.__sleep_mood = sleep_mood
        self.__health_rate = health_rate

    # sleep method
    def sleep(self, hours):
        if hours > 0:
            if hours > 7:
                print('lazy employee')
            elif hours < 7:
                print('tired employee')
            else:
                print('happy employee')
        else:
            print('enter a valid hours')

    # eat method
    def eat(self, meals):
        if meals == 3:
            self.set_health_rate(100)
        elif meals == 2:
            self.set_health_rate(75)
        elif meals == 1:
            self.set_health_rate(50)
        else:
            print('not valid')

    # buy method
    def buy(self, items):
        if items > 0:
            updated_money = self.get_money() - (10 * items)
            self.set_money(updated_money)

    # setter method for private attributes
    def set_health_rate(self, health_rate):
        if health_rate > 0 & health_rate < 100:
            self.__health_rate = health_rate
        else:
            print('enter a valid health rate in range of 0 : 100')

    def get_health_rate(self):
        return self.__health_rate

    def set_money(self, money):
        self.__money = money

    def get_money(self):
        return self.__money
