class Card:
    def __init__(self, name, attack, coin):
        self.__name = name
        self.__attack = attack
        self.__coin = coin
    def getName(self):
        return self.__name
    def getAttack(self):
        return self.__attack
    def getCoin(self):
        return self.__coin

class Viper(Card):
    def __init__(self):
        super(Viper, self).__init__(name='Viper', attack=1, coin=0)
class Scout(Card):
    def __init__(self):
        super(Scout, self).__init__(name='Scout', attack=0, coin=1)

class Explorer(Card):
    def __init__(self):
        super(Explorer, self).__init__(name='Explorer', attack=0, coin=2)
        self.__scrapUsed = False

    def scrapCard(self):
        print('here')
        self.__scrapUsed = True
        self.__attack = 2
        print(self.__attack)

    def getScrapUsed(self):
        return self.__scrapUsed

    def getAttack(self):
        return self.__attack