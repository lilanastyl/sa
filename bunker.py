import random
place = ["Море", "Гори", "Поле"]
square = ["12333", "232323", "3232132"]
food = ["Много", "Достаточно", "Мало"]


class Bunker():
    def __init__(self):
        self.place = place[random.randint(0, 2)]
        self.square = square[random.randint(0, 2)]
        self.food = food[random.randint(0, 2)]

