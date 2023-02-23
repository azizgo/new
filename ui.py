from accessify import private, protected

class Card:
    def __init__(self) -> None:
        self.name = 'Salom'
        self._balans = 122
        self.__pin = 1111

    @property
    @classmethod
    def getPin(self):
        return self.__pin


c = Card()
print(c.name)
print(c._balans)
c.__pin = 1000
print(c.getPin())
print(c.__pin)