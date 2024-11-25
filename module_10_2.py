import threading
import time

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} на нас напали!')
        enemy = 100
        days = 0
        while enemy > 0:
            enemy -= self.power
            time.sleep(1)
            days += 1
            print(f'{self.name} сражается {days} день(дня)..., осталось {enemy} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')