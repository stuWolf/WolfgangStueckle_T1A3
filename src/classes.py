class Person:
    def __init__(self, age = 26,shoesize = 0):
        self._age = age
        self._shoesize = shoesize

    # def __init__(self, shoesize = 0):
    #     self._shoesize = shoesize

    def get_age(self):
        return self._age

    def set_age(self, newAge):
        if (newAge > 0):
            self._age = newAge
        else:
            print ("New age is not valid!")

    def print_age(self):
        print(f'my age is{self._age}')

def output():
    alex = Person()

    alex.print_age()

    print(alex.get_age())

    alex.set_age(-1)

    print(alex.get_age())

    alex.set_age(27)

    print(alex.get_age())

output()