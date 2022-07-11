# Inheritance
class SchoolMember:
    """Represents any school member."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        """Tell my details."""
        print('Your name is: {} Age: {} years'.format(self.name, self.age), end=".. ")


class Teacher(SchoolMember):
    """Represents a teacher."""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Your Salary is: {:d}'.format(self.salary))


class Student(SchoolMember):
    """Represents a student."""

    def __init__(self, name, age, GPA):
        SchoolMember.__init__(self, name, age)
        self.GPA = GPA
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Your current GPA is: {}'.format(self.GPA))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 3.5)

# prints a blank line
print()

members = [t, s]
for member in members:
    # Works for both Teachers and Students
    member.tell()

# The SchoolMember class in this situation is known as the base class or the superclass. The Teacher and Student
# classes are called the derived classes or subclasses.
