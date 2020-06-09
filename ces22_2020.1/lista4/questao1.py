
# Classe abstrata para o motor
class AbstractEngine:
    def make_noise(self):
        raise NotImplementedError

# Implementação dos motores
class ElectricEngine(AbstractEngine):
    def make_noise(self):
        print('I am a electric engine. I don\'t make noise, sorry :/')

class CombustionEngine(AbstractEngine):
    def make_noise(self):
        print('Vrumm vrummm')

class HybridEngine(AbstractEngine):
    def make_noise(self):
        print('Sometimes I make noise but sometimes I don\'t. Am I bipolar?')

# Classe abstrata para os veículos
class AbstractVehicle:
    def __init__(self, vEngine):
        self.engine = vEngine

    def getVehicleType(self):
        print(self.__class__.__name__)

# Implementação dos veículos
class Car(AbstractVehicle):
    def __init__(self, carEngine = CombustionEngine()):
        super().__init__(carEngine)

class Truck(AbstractVehicle):
    def __init__(self, truckEngine = CombustionEngine()):
        super().__init__(truckEngine)

class Motocycle(AbstractVehicle):
    def __init__(self, motocycleEngine = CombustionEngine()):
        super().__init__(motocycleEngine)

if __name__ == "__main__":
    #---------------------------------------
    print()
    print('Standard car engine making noise: ')
    car = Car()
    car.engine.make_noise()
    #---------------------------------------
    print()
    print('Electric car engine making noise: ')
    electricCar = Car(ElectricEngine())
    electricCar.engine.make_noise()
    #---------------------------------------
    print()
    print('Hybrid truck engine making noise: ')
    hybridTruck = Truck(HybridEngine())
    hybridTruck.engine.make_noise()

    print()
