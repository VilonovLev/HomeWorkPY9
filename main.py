# 1. Создать класс TrafficLight (светофор):
# ● определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт.

import time


class TrafficLight:
    def __init__(self):
        self.__color = ['\U0001F7E5', '\U0001F7E8', '\U0001F7E9']

    def running(self):
        while True:
            ind = 2 if self.__color[0] == '\U0001F7E8' else 4
            self.__color.insert(ind, self.__color[0])
            print(self.__color.pop(0))
            time.sleep(2 if ind == 2 else 7)


t = TrafficLight()
t.running()


# 2. Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    __square_m = 25

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def asphalt_weight(self, depth):
        result = self.__length * self.__width * Road.__square_m * depth/1000
        return f'На эту дорогу необходимо {result} тонн'


road = Road(5000, 20)
print(road.asphalt_weight(5))


# Морской бой

class SedMap:
    field = [["." for _ in range(10)] for _ in range(10)]

    def sink(self, row, col, last_hit=("", "")):
        for x in range(row - 1, row + 2):
            if x < 0 or len(self.field) - 1 < x:
                continue
            for y in range(col - 1, col + 2):
                if y < 0 or len(self.field) - 1 < y:
                    continue
                elif last_hit[0] == x and last_hit[1] == y:
                    continue
                elif self.field[x][y] == "x":
                    self.sink(x, y, (row, col))
                else:
                    self.field[x][y] = "*"

        self.field[row][col] = "x"

    def shoot(self, row, col, result):
        if result == "hit":
            self.field[row][col] = "x"
        elif result == "sink":
            self.sink(row, col)
        else:
            self.field[row][col] = "*"

    def cell(self, row, col):
        return self.field[row][col]


sm = SedMap()
sm.shoot(0, 0, "sink")
sm.shoot(0, 9, "miss")
sm.shoot(1, 0, "sink")
sm.shoot(9, 9, "sink")
sm.shoot(5, 4, "hit")
sm.shoot(5, 5, "hit")

for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end=' ')
    print()
