from time import sleep
from datetime import datetime as dt


class TrafficLight:
    _states = {'Красный': 7, 'Желтый': 2, 'Зеленый': 10}
    _color = ''

    def running(self):
        for color, sw_time in self._states.items():
            self._color = color
            start_state_time = dt.now()

            print(f"Cветофор переключился в положение '{self._color}' "
                  f"На {sw_time} секунд")

            sleep(sw_time)

            print(f"Светофор находился в положении '{self._color}' " 
                  f"{(dt.now() - start_state_time).seconds} секунд")


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()
