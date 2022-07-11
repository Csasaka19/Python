# Properties: normally setters and getters can only be used on private attributes otherwise interphase is broken
# but when @properties is used this all changes it can even be used on public ones
class P:
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


p1 = P(1001)
print(p1.x)

p1.x = -12
print(p1.x)


# Two things are noteworthy: I just put the code line "self.x = x" in the __init__ method and the property method x
# is used to check the limits of the values. The second interesting thing is that "two" methods are written with the
# same name and a different number of parameters "def x(self)" and "def x(self,x)"
# It works here due to the decorating, otherwise it normally does not work

# Another one!!
class OurClass:
    def __init__(self, a):
        self.OurAtt = a

    @property
    def OurAtt(self):
        return self.__OurAtt

    @OurAtt.setter
    def OurAtt(self, val):
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val


x = OurClass(10)
print(x.OurAtt)
