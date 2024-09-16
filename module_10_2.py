# Задача "За честь и отвагу!"
import threading
from threading import Thread
import time


# Класс Knight, наследованный от Thread
class Knight(Thread):
    # Используем встроенный класс Lock() для вывода сообщений в любой момент времени, не смешивая их из разных потоков
    print_LCK = threading.Lock()

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.warriors = 100
        self.days = 0

    # Метод run отвечает за выполнение логики работы потока (сражение рыцаря с врагами)
    def run(self):

        # Выводим сообщение о начале сражения для данного рыцаря
        print(f"{self.name}, на нас напали!")

        # Сражение будет продолжаться, пока количество врагов больше 0
        while self.warriors > 0:

            # При каждом проходе цикла идет задержка в 1 секунду для моделирования одного дня сражения
            time.sleep(1)

            # Количество врагов уменьшаем на значение power рыцаря и увеличиваем количество дней сражения
            self.warriors -= self.power
            self.days += 1

            # Синхронизация вывода и предотвращение одновременного доступа нескольких потоков к функции print
            with Knight.print_LCK:

                # Если врагов еще не побеждено, выводим сообщение о текущем дне сражения и оставшемся количестве врагов
                if self.warriors > 0:
                    print(f"{self.name} сражается {self.days} день(дня)..., осталось {max(self.warriors, 0)} воинов.")

                # Если все враги побеждены, выводим сообщение о победе рыцаря и количестве дней, потребовавшихся для победы
                else:
                    print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print('Все битвы закончились!')
