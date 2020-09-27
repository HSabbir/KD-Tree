class Mammal(object):
    def __init__(self, mamalName, leg_no):
        self.name = mamalName
        self.leg_no = leg_no

    def print(self):
        print(self.name, 'has', self.leg_no, 'legs')
        print(self.name, 'is warm-blooded animal')

class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self,'Dog',4)

class Human(Mammal):
    def __init__(self):
        Mammal.__init__(self,'Human',2)


d1 = Dog()
print('***********')
d1.print()
h1 = Human()
print('***********')
h1.print()
