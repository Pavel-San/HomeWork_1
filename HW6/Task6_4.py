class Car():

    def __init__(self, max_speed, color, name, is_police):
        self.max_speed = max_speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Создан новый автомобиль {name}, цвет {color}')

    def show_speed(self, speed):
        self.speed = speed
        print(f'Скорость движения {self.speed} км/ч')
        if self.speed > self.max_speed and not self.is_police:
            print('Внимание! Превышение допустимой скорости!')

    def go(self):
        print(f'{self.name} начал движение')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        print(f'{self.name} повернул {direction}')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Это семейный автомобиль')

    def show_speed(self, speed):
        self.speed = speed
        super().show_speed(self.speed)


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Это спортивный автомобиль')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Это служебный автомобиль')

    def show_speed(self, speed):
        self.speed = speed
        super().show_speed(self.speed)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Это полицейский автомобиль')


my_family_car = TownCar(60, 'черный', 'KIA Carnival', False)
my_family_car.go()
my_family_car.show_speed(40)
my_family_car.show_speed(50)
my_family_car.show_speed(60)
my_family_car.turn('направо')
my_family_car.turn('налево')
my_family_car.stop()
print()

my_work_car = WorkCar(60, 'серый', 'Lada Largus', False)
my_work_car.go()
my_work_car.show_speed(40)
my_work_car.stop()
print()

police_car = PoliceCar(0, 'белый', 'Toyota Camry', True)
print()

sport_car = SportCar(60, 'черный', 'Ferrari Testarossa', False)
sport_car.go()
sport_car.show_speed(60)
sport_car.show_speed(70)
police_car.go()
police_car.show_speed(80)
police_car.turn('налево')
police_car.turn('направо')
police_car.stop()
sport_car.stop()
