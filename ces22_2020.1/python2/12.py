import abc
class Animal:
    def __init__(self, name : str):
        for c in name:
            if not c.isalnum():
                raise Exception('Invalid symbol for animal name: {}'.format(c))
        self.name = name

    @abc.abstractmethod
    def speak(self):
        raise NotImplementedError

class Cat(Animal):
    def speak(self):
        from random import randint
        r = randint(0, 100)
        print('meoow! Now my name is a random number because python can handle to duck type.\n' + \
             'my old name: {} \nmy new name: {}\n'.format(self.name, r))
        self.name = r

class Dog(Animal):
    def speak(self):
        print('woof! WOOF! I\'m {} and I am a gud boi\n'.format(self.name))

print()
cat = Cat('Antony')
cat.speak()
cat.speak()
print()
dog = Dog('Leophony')
dog.speak()
# Raises a exception:
#dog = Dog('le!o')
