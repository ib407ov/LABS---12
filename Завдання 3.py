class Masiv:
    def __init__(self, *args):
        if len(args) == 0:
            self.masiv = []
        else:
            self.masiv = []
            for i in range(len(args)):
                self.masiv.append(args[i])


    def __getitem__(self, key):  # --- Для зчитування значення за індексом
        for i in range(len(self.masiv)):
            if i == key:
                return self.masiv[i]

    def __setitem__(self, key, value):  # --- Для встановлення значення за індексом
        for i in range(len(self.masiv)):
            if i == key:
                self.masiv[i] = value

    def printMasiv(self):
        return print(self.masiv)

    def inputMasiv(self):
        for i in range(len(self.masiv)):
            v[i] = input('el {0} = '.format(i))

    def minElement(self):
        return print(min(self.masiv))

    def maxElement(self):
        return print(max(self.masiv))


v = Masiv(2, 3, 6, 2, 3)
v.printMasiv()
v.inputMasiv()
v.printMasiv()
v.minElement()
v.maxElement()
# for i in range(3):
#     print('el = ', v[i])
#
# for i in range(3):
#     v[i] = input('el{0} = '.format(i))

