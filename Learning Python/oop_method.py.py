class Person:
    def say_hi(self):  # Just as a function only that it has the self attribute
        print('Hello, how are you?')


p = Person()
p.say_hi()
# The previous 2 lines can also be written as
# Person().say_hi()
