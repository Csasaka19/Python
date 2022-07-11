# The attribute x can have values between 0 and 1000. If a value larger than 1000 is assigned, x should be set to
# 1000. Correspondingly, x should be set to 0, if the value is less than 0.
class P:
    def __init__(self, x):
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


p1 = P(1001)
print(p1.get_x())

p3 = P(-1)
print(p3.get_x())

p2 = P(15)
print(p2.get_x())
