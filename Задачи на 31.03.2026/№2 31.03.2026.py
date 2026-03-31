class Car:
    def move(self):
        print("Автомобиль едет по дороге")

class Bicycle:
    def move(self):
        print("Велосипед едет по велодорожке")

def move_vehicles(vehicles):
    for vehicle in vehicles:
        vehicle.move()