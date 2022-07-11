class Animalia:  # The super class

    def __init__(self, appearance="Not known", bloodtype="Not known", birth="Not known", residence="Not Known"):
        self.__appearance = appearance
        self.__bloodtype = bloodtype
        self.__birth = birth
        self.__residence = residence

    # Property setter and property getters are used to access and assign the attributes
    # and instances which are private

    @property
    def Appearance(self):
        return self.__appearance

    @Appearance.setter
    def Appearance(self, appearance):
        self.__appearance = appearance

    @property
    def Bloodtype(self):
        return self.__bloodtype

    @Bloodtype.setter
    def Bloodtype(self, bloodtype):
        self.__bloodtype = bloodtype

    @property
    def Birth(self):
        return self.__birth

    @Birth.setter
    def Birth(self, birth):
        self.__birth = birth

    @property
    def Residence(self):
        return self.__residence

    @Residence.setter
    def Residence(self, residence):
        self.__residence = residence

    def __str__(self):  # Override to print out a string to the stdout
        return "It is covered in {} ,and is {}.Born through {} as its means" \
               "and it resides in {}".format(self.__appearance, self.__bloodtype, self.__birth, self.__residence)


# Subclasses which inherit from the super class appear here
# You can inherit from multiple classes by separating
# the classes with a comma in the parentheses e.g Class Mam-alia(Animalia, Chordata, Living)
# this is multiple inheritance

class Mamalia(Animalia):

    def __init__(self, appearance="Not known", bloodtype="Not known", birth="Not known", residence="Not Known"):
        super().__init__(appearance, bloodtype, birth, residence)
        self.__Take = None

    def __int__(self, appearance="fur/hair",
                bloodtype="Warmblooded",
                birth="either from the womb or eggs are laid",
                residence="landscapes and tress",
                Take=True):
        # Call the init method from the super class to initialize the parameters
        Animalia.__init__(self, appearance, bloodtype, birth, residence)

        self.__Take = Take

    # Property setter and property getters are used to access and assign the attributes
    # and instances which are private present in this class Take
    @property
    def Care(self):
        return self.__Take

    @Care.setter
    def Care(self, Take):
        self.__Take = Take

    def __str__(self):
        return super().__str__() + " it really is {} it takes care of its young ones" \
            .format(self.__Take)


class Reptilia(Animalia):

    def __init__(self, appearance="scales",
                 bloodtype="Cold-Blooded",
                 birth="eggs are laid some even burst!!",
                 residence="landscapes ,tress and holes",
                 Survival="the young ones are left to fight for their lives"):
        Animalia.__init__(self, appearance, bloodtype, birth, residence)

        self.__survival = Survival

    # Property setter and property getters are used to access and assign the attributes
    # and instances which are private present in this class survival
    @property
    def Survival(self):
        return self.__survival

    @Survival.setter
    def Survival(self, Survival):
        self.__survival = Survival

    def __str__(self):
        return super().__str__() + " it really leaves {} how sadistic" \
            .format(self.__survival)


class Fish(Animalia):

    def __init__(self, appearance="scales",
                 bloodtype="Cold-Blooded",
                 birth="eggs are laid",
                 residence="water bodies",
                 ditch="they just lay the eggs and swim away!!"):
        Animalia.__init__(self, appearance, bloodtype, birth, residence)

        self.__ditch = ditch

    # Property setter and property getters are used to access and assign the attributes
    # and instances which are private present in this class ditch
    @property
    def Ditch(self):
        return self.__ditch

    @Ditch.setter
    def Ditch(self, ditch):
        self.__ditch = ditch

    def __str__(self):
        return super().__str__() + " {} Very comical.." \
            .format(self.__ditch)


class Amphibia(Animalia):

    def __init__(self, appearance="scales and moist skin",
                 bloodtype="Cold-Blooded",
                 birth="eggs are laid",
                 residence="water bodies",
                 unique="they creep me out!!!"):
        Animalia.__init__(self, appearance, bloodtype, birth, residence)

        self.__unique = unique

    # Property setter and property getters are used to access and assign the attributes
    # and instances which are private present in this class unique
    @property
    def Unique(self):
        return self.__unique

    @Unique.setter
    def Unique(self, unique):
        self.__unique = unique

    def __str__(self):
        return super().__str__() + " {} <<<.." \
            .format(self.__unique)

        # Operator overloading isn't necessary in Python because
        # Python allows you to enter unknown numbers of values
        # Always make sure self is the first attribute in your
        # class methods

    def sumAll(self, *args):
        sumer = 0

        for i in args:
            sumer += i

        return sumer


animal1 = Animalia()

print(animal1.Appearance)
print(animal1.Birth)
print(animal1.Bloodtype)
print(animal1.Residence)

# Call __str__()
print(animal1)
print()  # Prints a blank line

Jackal = Mamalia("fur/hair", "Warmblooded", "either from the womb or eggs are laid", "landscapes and tress")

print(Jackal.Appearance)
print(Jackal.Bloodtype)
print(Jackal.Birth)
print(Jackal.Residence)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

Lizard = Reptilia()

print(Lizard.Birth)
print(Lizard.Appearance)
print(Lizard.Survival)
print(Lizard.Residence)
print(Lizard.Bloodtype)
print(Lizard)
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

Salamander = Amphibia()

print(Salamander.Birth)
print(Salamander.Bloodtype)
print(Salamander.Unique)
print(Salamander)

print('..........................................................')

# Operator overloading in Python
print("Sum : {}".format(Salamander.sumAll(1, 2, 3, 4, 5, 38, 49, 77)))


# Polymorphism in Python works differently from other
# languages in that functions accept any object
# and expect that object to provide the needed method

# This isn't something to dwell on. Just know that
# if you call on a method for an object that the
# method just needs to exist for that object to work.
# Polymorphism is a big deal in other languages that
# are statically typed (type is defined at declaration)
# but because Python is dynamically typed (type defined
# when a value is assigned) it doesn't matter as much.

def getBirthType(theObject):
    print("The {} is {}".format(type(theObject).__name__,
                                theObject.Birth))  # Birth exists so it works


getBirthType(Lizard)
getBirthType(Salamander)

print()

def getAppearance(theObject):
    print("The {} is {}".format(type(theObject).__name__,
                                theObject.Appearance))  # Appearance exists so it works


getAppearance(Lizard)
getAppearance(Salamander)
getAppearance(Jackal)
