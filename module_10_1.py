# Задача "Потоковая запись в файлы"

# Импортруем необходимые библиотеки
import time
import threading

# Создаем Функцию wite_words, которая принимает два аргумента: количество слов word_count и имя файла file_name,
# в который будут записаны слова
def wite_words(word_count, file_name):

    # Создаем файл с указанным именем, в который записываются слова с паузой в 0.1 секунды между каждой записью
    with open(file_name, 'w', encoding="UTF-8") as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    # Выводим сообщение об окончании записи в файл
    print(f"Завершилась запись в файл {file_name}")

# Вызываем функцию последовательно 4 раза, передавая ей различные аргументы
start_time = time.time()
wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")
print(f"Время выполнения функций: {time.time() - start_time} секунд")

# Создаем четыре потока, которые выполняют ту же функцию с другими значениями
threads = []
file_args = [
    (10, "example5.txt"),
    (30, "example6.txt"),
    (200, "example7.txt"),
    (100, "example8.txt")
]

start_time = time.time()
for args in file_args:
    thread = threading.Thread(target=wite_words, args=args)
    threads.append(thread)
    thread.start()

# Ждем завершения всех созданных потоков
for thread in threads:
    thread.join()

print(f"Время выполнения потоков: {time.time() - start_time} секунд")
