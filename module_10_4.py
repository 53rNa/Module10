# Задача "Потоки гостей в кафе"

import random
import time
from threading import Thread
from queue import Queue


# Класс Table хранит информацию о находящемся за ним гостем (Guest)
class Table:
    def __init__(self, number):
        # Номер стола
        self.number = number

        # гость, который сидит за этим столом (по умолчанию None - т.е никого нет)
        self.guest = None

# Класс Guest представляет собой гостя в кафе, ожидающего определённое время (принимает пищу)
# Наследуется от Thread, получается, что каждый гость - это поток
class Guest(Thread):
    def __init__(self, name):
        super().__init__()

        # Имя гостя
        self.name = name

    # Метод run, который выполняется при запуске потока. В нем происходит ожидание случайным образом от 3 до 10 секунд
    def run(self):
        wait_time = random.randint(3, 10)

        # Имитация время ожидания (приема пищи)
        time.sleep(wait_time)

# Класс кафе
class Cafe:
    def __init__(self, *tables):

        # Очередь для гостей
        self.queue = Queue()

        # Столы в кафе
        self.tables = list(tables)

    # Метод распределяет прибывших гостей по столам
    def guest_arrival(self, *guests):

        # Для каждого гостя проверяет наличие свободного стола
        for guest in guests:
            available_table = next((t for t in self.tables if t.guest is None), None)

            # Если стол свободен, сажаем гостя за этот стол, запускаем его поток,
            # и выводим сообщение, что гость сел за стол
            if available_table:
                available_table.guest = guest
                print(f"{guest.name} сел(-а) за стол номер {available_table.number}")
                # Запускаем поток
                guest.start()

            # Если свободных столов нет, гость - в очередь, и выводим сообщение, что гость в очереди
            else:
                print(f"{guest.name} в очереди")

                # # Добавляем гостя в очередь
                self.queue.put(guest)

    # Метод обслуживания гостей
    def discuss_guests(self):

        # Пока есть гости в очереди или хотя бы один стол занят
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:

                # Если за столом есть гость и он уже завершил прием пищи
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")

                    # Освобождаем стол
                    table.guest = None

                # Если стол свободен и есть гости в очереди
                if table.guest is None and not self.queue.empty():

                    # Берём гостя из очереди
                    next_guest = self.queue.get()

                    # Сажаем его за стол
                    table.guest = next_guest
                    print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

                    # Запускаем поток для нового гостя
                    next_guest.start()

            # Делаем паузу перед следующей проверкой
            time.sleep(1)

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]


# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()

print("Все гости ушли)")
