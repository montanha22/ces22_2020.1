from questao1 import *

# abstract Factory
class AbstractCreator():
    def __init__(self):
        pass
    def createVehicle(self):
        raise NotImplementedError 

# factory Implementations
class ElectricEngineCarCreator(AbstractCreator):
    def __init__(self):
        pass
    def createVehicle(self):
        return Car(ElectricEngine())

class HybridTruckCreator(AbstractCreator):
    def __init__(self):
        pass
    def createVehicle(self):
        return Truck(HybridEngine())

class CombustionMotocycleCreator(AbstractCreator):
    def __init__(self):
        pass
    def createVehicle(self):
        return Motocycle()

if __name__ == "__main__":
    # criando um carro de motor elétrico utilizando a fábrica
    eCarCreator = ElectricEngineCarCreator() 
    print('-----------------------')
    print('electric car making noise:')
    eCar = eCarCreator.createVehicle()
    eCar.engine.make_noise()
    print('showing vehicle type: ')
    eCar.getVehicleType()


    # Criando um caminhão híbrido usando a fábrica
    hTruckCreator = HybridTruckCreator()
    hTruck = hTruckCreator.createVehicle()
    print('-----------------------')
    print('hybrid truck engine making noise:')
    hTruck.engine.make_noise()
    print('showing vehicle type:')
    hTruck.getVehicleType()

    # Criando um caminhão híbrido usando a fábrica
    cMotoCreator = CombustionMotocycleCreator()
    cMoto = cMotoCreator.createVehicle()
    print('-----------------------')
    print('combustion motocycle engine making noise:')
    cMoto.engine.make_noise()
    print('showing vehicle type:')
    cMoto.getVehicleType()
    print('-----------------------')