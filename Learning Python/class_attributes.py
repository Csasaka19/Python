# Class attributes: Private , public and protected
# Private: abbreviated by __ can only be accessed by the owner
# Protected(restricted): abbreviated by _  can be accessed at users risk
class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"

    @property  # property
    def prot(self):
        return self._prot


x = A()
print(x.pub + "  you can change me anytime and anywhere, however you like")
print(x.prot)  # I have used it irrespective of the risks heeh!
# print(x.__priv) an error occurs when this is printed showing it does not exist and can only be accessed through
# encapsulation getters and setters


