from vehicles import (
    CarFactory,
    MotorcycleFactory,
    TruckFactory,
    BusFactory
)


def create_vehicle_from_user():

    # Выбор типа транспортного средства
    print("Choose vehicle type:")
    print("1 - Car")
    print("2 - Motorcycle")
    print("3 - Truck")
    print("4 - Bus")

    choice = input("Enter choice: ")

    if choice == "1":

        # Ввод данных для автомобиля
        brand = input("Enter brand: ")
        model = input("Enter model: ")
        fuel = input("Enter fuel type: ")

        factory = CarFactory(brand, model, fuel)

    elif choice == "2":

        # Ввод данных для мотоцикла
        moto_type = input("Enter motorcycle type: ")
        engine = input("Enter engine volume: ")

        factory = MotorcycleFactory(moto_type, engine)

    elif choice == "3":

        # Ввод данных для грузовика
        capacity = input("Enter capacity (tons): ")
        axles = input("Enter number of axles: ")

        factory = TruckFactory(capacity, axles)

    elif choice == "4":

        # Ввод данных для автобуса
        seats = input("Enter number of seats: ")
        fuel = input("Enter fuel type: ")

        factory = BusFactory(seats, fuel)

    else:
        # Неверный выбор
        print("Invalid choice")
        return

    # Создание транспортного средства через фабрику
    vehicle = factory.create_vehicle()

    # Использование транспортного средства
    vehicle.drive()
    vehicle.refuel()


# Точка входа в программу
if __name__ == "__main__":

    # Цикл для создания нескольких транспортных средств
    while True:

        create_vehicle_from_user()

        again = input("Create another vehicle? (yes/no): ")

        # Проверка, хочет ли пользователь создать ещё одно ТС
        if again.lower() != "yes":
            break
