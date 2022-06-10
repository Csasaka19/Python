# Object-oriented programming intro
# Classes: a blueprint of creating objects
# Objects: are created from classes
class Student:

    def __init__(self, name, major, identification, age, gender):
        self.name = name
        self.major = major
        self.identification = identification
        self.age = age
        self.gender = gender

    def call(self, hobby, club):
        print(
            "\n{} is a student here pursuing {}, he is identified by {} id no.He is {} years old and is a vibrant "
            "young {}".format(self.name, self.major, self.identification, self.age, self.gender))
        print("His major hobby is {}, thus he belongs to the {} club".format(hobby, club))


Student_1 = Student("Clive Sasaka", "Computer Science", 234598, 21, "Alpha_Male")  # Student_1 is an object
print(Student_1)  # This actually prints the memory location of the object
# this can be overridden by:
# def __str__(self) -> str:
# return super().__str__() to print the actual contents of the class .... the override is shown below

print(f"\n\nWhat a name: {Student_1.name}")
print(f"He is an :{Student_1.gender}")
print(f"He is identified by: {Student_1.identification} no.")
print(f"The course pursued is: {Student_1.major}")
print(f"The age of this student is: {Student_1.age}")
Student_1.call("Playing chess", "Chess")

print("\n After override")

class Student:

    def __init__(self, name, major, identification, age, gender):
        self.name = name
        self.major = major
        self.identification = identification
        self.age = age
        self.gender = gender

    def call(self, hobby, club):
        print(
            "\n{} is a student here pursuing {}, he is identified by {} id no.He is {} years old and is a vibrant "
            "young {}".format(self.name, self.major, self.identification, self.age, self.gender))
        print("His major hobby is {}, thus he belongs to the {} club".format(hobby, club))

    def __str__(self) -> str:  # forces string to be written by default
        return f"\nName is: {self.name},\nMajor is: {self.major},\nIdentification is: {self.identification},\nAge is: {self.age},\nGender is: {self.gender} "


Student_1 = Student("Clive Sasaka", "Computer Science", 234598, 21, "Alpha_Male")  # Student_1 is an object
print(Student_1)  # This actually prints the actual value is written after the override
# this can be overridden by:
# def __str__(self) -> str:
# return super().__str__() to print the actual contents of the class as shown here

print(f"\n\nWhat a name: {Student_1.name}")
print(f"He is an :{Student_1.gender}")
print(f"He is identified by: {Student_1.identification} no.")
print(f"The course pursued is: {Student_1.major}")
print(f"The age of this student is: {Student_1.age}")
Student_1.call("Playing chess", "Chess")