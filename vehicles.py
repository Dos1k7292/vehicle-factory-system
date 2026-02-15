from abc import ABC, abstractmethod

# =========================
# Интерфейс IVehicle
# =========================

class IVehicle(ABC):

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass


# =========================
# Конкретные транспортные средства
# =========================

class Car(IVehicle):

    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def drive(self):
        print(f"Car {self.brand} {self.model} is driving.")

    def refuel(self):
        print(f"Car is refueling with {self.fuel_type}.")


class Motorcycle(IVehicle):

    def __init__(self, moto_type, engine_volume):
        self.moto_type = moto_type
        self.engine_volume = engine_volume

    def drive(self):
        print(f"{self.moto_type} motorcycle with {self.engine_volume}cc is driving.")

    def refuel(self):
        print("Motorcycle is refueling.")


class Truck(IVehicle):

    def __init__(self, capacity, axles):
        self.capacity = capacity
        self.axles = axles

    def drive(self):
        print(f"Truck with {self.capacity} tons capacity is driving.")

    def refuel(self):
        print("Truck is refueling.")


# НОВОЕ транспортное средство (Автобус)
class Bus(IVehicle):

    def __init__(self, seats, fuel_type):
        self.seats = seats
        self.fuel_type = fuel_type

    def drive(self):
        print(f"Bus with {self.seats} seats is driving.")

    def refuel(self):
        print(f"Bus is refueling with {self.fuel_type}.")


# =========================
# Базовый класс фабрики
# =========================

class VehicleFactory(ABC):

    @abstractmethod
    def create_vehicle(self):
        pass


# =========================
# Конкретные фабрики
# =========================

class CarFactory(VehicleFactory):

    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def create_vehicle(self):
        return Car(self.brand, self.model, self.fuel_type)


class MotorcycleFactory(VehicleFactory):

    def __init__(self, moto_type, engine_volume):
        self.moto_type = moto_type
        self.engine_volume = engine_volume

    def create_vehicle(self):
        return Motorcycle(self.moto_type, self.engine_volume)


class TruckFactory(VehicleFactory):

    def __init__(self, capacity, axles):
        self.capacity = capacity
        self.axles = axles

    def create_vehicle(self):
        return Truck(self.capacity, self.axles)


class BusFactory(VehicleFactory):

    def __init__(self, seats, fuel_type):
        self.seats = seats
        self.fuel_type = fuel_type

    def create_vehicle(self):
        return Bus(self.seats, self.fuel_type)
