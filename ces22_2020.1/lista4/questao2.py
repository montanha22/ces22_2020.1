# Classe component base para os ingredientes
class PizzaComponent:
    cost = 0
    def getDescription(self):
        return self.__class__.__name__
    
    def getTotalCost(self):
        return self.__class__.cost

# Nosso ingrediente concreto
class Mass(PizzaComponent):
    cost = 5

# Nosso decorator para os outros ingredientes
class Decorator(PizzaComponent):
    def __init__(self, pizzaComponent):
        self.component = pizzaComponent

    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + ', ' + PizzaComponent.getDescription(self)

# Nossos outros ingredientes
class Cheese(Decorator):
    cost = 2
    def __init__(self, pComponent):
        Decorator.__init__(self, pComponent)

class Tomato(Decorator):
    cost = 0.75
    def __init__(self, pComponent):
        Decorator.__init__(self, pComponent)

class Chicken(Decorator):
    cost = 3
    def __init__(self, pComponent):
        Decorator.__init__(self, pComponent)

class Egg(Decorator):
    cost = 2
    def __init__(self, pComponent):
        Decorator.__init__(self, pComponent)

class Ham(Decorator):
    cost = 2.5
    def __init__(self, pComponent):
        Decorator.__init__(self, pComponent)


# pizza de queijo
cheesePizza = Cheese(Mass())
print()
print('ingredients: ')
print(cheesePizza.getDescription())
print('\nprice: ')
print(cheesePizza.getTotalCost())
print()

# pizza portuguesa
portuguesePizza = Egg(Cheese(Ham(Tomato(Mass()))))
print()
print('ingredients: ')
print(portuguesePizza.getDescription())
print('\nprice: ')
print(portuguesePizza.getTotalCost())
print()