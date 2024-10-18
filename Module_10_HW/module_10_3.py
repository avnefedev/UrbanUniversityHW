from random import randint
from threading import Thread, Lock
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            a = randint(50, 500)
            self.balance += a
            print(f'Пополнение: {a}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for _ in range(100):
            a = randint(50, 500)
            print(f'Запрос на {a}')
            if a <= self.balance:
                self.balance -= a
                print(f'Снятие: {a}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств.')
                self.lock.acquire()

bk = Bank()

th_1 = Thread(target=Bank.deposit, args=(bk, ))
th_2 = Thread(target=Bank.take, args=(bk, ))

th_1.start()
th_2.start()

th_1.join()
th_2.join()

print(f'Баланс: {bk.balance}')
