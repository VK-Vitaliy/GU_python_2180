class Road:
    def __init__(self, length, width):
        '''
        :param length: asphalt length in meters
        :param width: asphalt width in meters
        '''
        self._length = length
        self._width = width
        self._weight = 25

    def asphalt_weight_in_tons(self, thickness):
        '''
        :param thickness: asphalt thickness in centimeters
        :return: asphalt weight in tons
        '''
        tons = self._length * self._width * self._weight * int(thickness) // 1000
        result = f'{self._length} м * {self._width} м * {self._weight} кг * {int(thickness)} см = {int(tons)} т.'
        return result


asphalt = Road(5000, 20)
print(asphalt.asphalt_weight_in_tons(5))
