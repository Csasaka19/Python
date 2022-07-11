# Setters and getters intro
class Robot:
    def __init__(self,name=None,build_year=None):
        self.name = name
        self.build_year = build_year

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
        if self.build_year:
            print("I was built in " + str(self.build_year))
        else:
            print("It's not known, when I was created!")

    def set_name(self, name): # setter
        self.name = name

    def get_name(self):  # getter
        return self.name

    def set_build_year(self, by):
        self.build_year = by

    def get_build_year(self):
        return self.build_year


x = Robot("Henry", 2008)
y = Robot()  # Nothing was passed but the setter and getter can be used because the same self method is used in both
# initialization(__init__)  set_name also set_build_year to get through the data
y.set_name("Marvin")
x.say_hi()
y.set_build_year(2014)
y.say_hi()
