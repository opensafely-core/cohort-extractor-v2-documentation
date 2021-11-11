class Person:
    """
    A Person Class contains a name
    """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """
        Saying hello is important
        """
        return f"hello, i am {self.name}"


class Farmer(Person):
    """
    A Farmer is an important member of society, and is a Person.
    All Farmers are Persons.
    """

    def __init__(self, name, crop):
        super().__init__(name)
        self.crop = crop

    def grow_crop(self):
        """
        I tell you the crops i grow
        """
        return f"I grow {self.crop}"
