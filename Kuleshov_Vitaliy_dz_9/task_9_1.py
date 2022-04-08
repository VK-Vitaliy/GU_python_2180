import time


class TrafficLight:
    __colors = ['red', 'yellow', 'green']

    def __init__(self, traffic_count=10):
        self.traffic_count = traffic_count  # настроим количество циклов

    def running(self):
        while True:
            print(self.__colors[0].upper())
            time.sleep(7)
            print(self.__colors[1].upper())
            time.sleep(2)
            print(self.__colors[2].upper())
            time.sleep(7)
            self.traffic_count -= 1
            if self.traffic_count == 0:  # сделаем выход из бесконечного цикла
                break


traffic_lights = TrafficLight(traffic_count=5)
traffic_lights.running()
