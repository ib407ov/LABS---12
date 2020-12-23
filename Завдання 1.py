import math
class TVektor2D:
    def __init__(self, *args):
        arguments_count = len(args)
        if arguments_count == 0:
            self.x1 = 0
            self.x2 = 0
            self.y1 = 1
            self.y2 = 1

        elif arguments_count == 1:
            self.x1 = args[0]
            self.x2 = 0
            self.y1 = 0
            self.y2 = 0

        elif arguments_count == 2:
            self.x1 = args[0]
            self.x2 = args[1]
            self.y1 = 0
            self.y2 = 0

        elif arguments_count == 3:
            self.x1 = args[0]
            self.x2 = args[1]
            self.y1 = args[2]
            self.y2 = 0

        else:
            self.x1 = args[0]
            self.x2 = args[1]
            self.y1 = args[2]
            self.y2 = args[3]

    @property
    def function(self):
        print('firs vektor = [{0}, {1}]'.format(self.x1, self.x2))
        print('second vektor = [{0}, {1}]'.format(self.y1, self.y2))

    @property
    def lehghtVekror(self):
        return print(math.fabs(math.sqrt(((self.x1 - self.y1) ** 2 ) + ((self.x2 - self.y2) ** 2))))

    @property
    def normalizationvektor(self):
        z = (math.pow(self.x1, 2) + math.pow(self.x2, 2) + (self.y1 ** 2) + (self.x2 ** 2))
        print('x1 = ', self.x1/z)
        print('x2 = ', self.x2/z)
        print('y1 = ', self.y1/z)
        print('y2 = ', self.y2/z)

    @property
    def comparison(self):
        A = math.sqrt(math.pow(self.x1, 2) + math.pow(self.x2, 2))
        B = math.sqrt(math.pow(self.y1, 2) + math.pow(self.y2, 2))
        A = math.fabs(A)
        B = math.fabs(B)
        return (A, B)
    def __add__(self, other):
        return TVektor2D(self.x1 + other,
                         self.x2 + other,
                         self.y1 + other,
                         self.y2 + other)

    def __sub__(self, other):
        return TVektor2D(self.x1 - other,
                         self.x2 - other,
                         self.y1 - other,
                         self.y2 - other)

    def __mul__(self, other):
        return TVektor2D(self.x1 * other,
                         self.x2 * other,
                         self.y1 * other,
                         self.y2 * other)

    def __getitem__(self, key):  # --- Для зчитування значення за індексом
        if key == 1:
            return self.x1
        elif key == 2:
            return self.x2
        elif key == 3:
            return self.y1
        elif key == 4:
            return self.y2
        else:
            raise Error("Wrong key")

    def __setitem__(self, key, value):  # --- Для встановлення значення за індексом
        if key == 1:
            self.x1 = value
        elif key == 2:
            self.x2 = value
        elif key == 3:
            self.y1 = value
        elif key == 4:
            self.y2 = value
        else:
            raise Error("Wrong key")

    def __delitem__(self, key):  # --- Видалення елемента за індексом
        if key == 1:
            del self.x1
        elif key == 2:
            del self.x2
        elif key == 3:
            del self.y1
        elif key == 4:
            del self.y2
        else:
            raise Error("Wrong key")

v = TVektor2D(2,4,6,8)
print('x=', v[3])
v[2] = 17
v.function
del v[2]
v[2] = 10
v.function