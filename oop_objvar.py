# Note that an object variable with the same name as a class variable will hide the class variable!
class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):  # object
        """Initializes the data."""
        self.name = name  # name is an object variable
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod  # @classmethod decorator is the same as calling: how_many = classmethod(how_many)
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robot(s).".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("CLI--Gro#@-_id")
droid2.say_hi()
Robot.how_many()

droid3 = Robot("C-3PO")
droid3.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.\n")
droid1.die()
droid2.die()
droid3.die()

Robot.how_many()
# NB: self.__class__.population can replace Robot.population because every object refers to its class via the
# self.__class__ attribute.

# All class members are public. One exception: If you use data members with names using the double underscore prefix
# such as __privatevar, Python uses name-mangling to effectively make it a private variable.
