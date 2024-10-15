from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.bot = 100

    def run(self):
        day = 0
        print(f'{self.name} на нас напали!')
        while self.bot > 0:
            self.bot -= self.power
            day += 1
            time.sleep(1)
            print(f'{self.name} сражается {day}... осталось {self.bot} воинов')
        else:
            print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Битва закончилась')

