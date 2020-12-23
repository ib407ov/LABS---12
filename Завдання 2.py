class TMoney:
    def __init__(self, *args):
        arreyArgs = len(args)
        if arreyArgs == 0:
            self.dolarsMy = float(0)
            self.grivna = float(0)

        elif arreyArgs == 1:
            self.dolarsMy = float(args[0])
            self.grivna = float(0)

        else:
            self.dolarsMy = float(args[0])
            self.grivna = float(args[1])

    # метод додавання
    def addMoney(self, _money, _dolarExchange):
        money = _money // _dolarExchange
        money = money + self.dolarsMy
        return print('You have dolars : ', money)

    # вилучення гошей вказуючи суму в гривнях
    def withdrawalMoney(self, _money, _dolarExchange):
        money = _money // _dolarExchange
        self.dolarsMy -= money
        return print('You have dolars : ', self.dolarsMy)

    # визначення курсу долара при якому еквівалент гривень,
    # збільшится по відношенню до долара на 100
    def grivnaX100(self, _dolars):
        dolars = _dolars / 10
        return print('Dolar exchange rate : ', dolars)

    # рядкове представлення даних об’єкта
    def ToString(self):
        A = [self.dolarsMy, self.grivna]
        return print(A)

dolars = float(input('Dolar exchange rate : '))
g = TMoney(10, 50)
g.addMoney(100, dolars)
g.withdrawalMoney(100, dolars)
g.grivnaX100(dolars)
g.ToString()