# Static methods and class methods' intro staticmethod does not have a first parameter with a reference to an object.
# Class method unlike static methods class methods are bound to a class. The first parameter of a class method is a
# reference to a class and can be called by instance or class name
# Class methods have more advantage than static ones as they are more dynamic
class Pet:
    _class_info = "pet animals"

    @classmethod
    def about(cls):
        print("This class is about " + cls._class_info + "!")


class Dog(Pet):
    _class_info = "man's best friends"


class Cat(Pet):
    _class_info = "all kinds of cats"


Pet.about()  # prints the class info itself
Dog.about()  # prints the subclass dog after override
Cat.about()  # prints the subclass cat after override

# The differences ps..... not related to the above source code
# str()	                                repr()
# make object readable	             need code that reproduces object
# generate output for end user	     generate output for developer
