# Задача "Многопроцессное считывание"

import time
from multiprocessing import Pool


def read_info(name):
    # Создаем локальный список
    all_data = []

    # Открываем файл для чтения
    with open(name, 'r') as file:
        # Считываем информацию построчно (readline), пока считанная строка не окажется пустой
        while True:
            # Считываем строку
            line = file.readline()

            # Если строка пустая, выходим из цикла
            if not line:
                break

            # Добавляем строку в список, удаляя символы новой строки
            all_data.append(line.strip())


# Создаем список названий файлов в соответствии с названиями файлов находящихся в архиве (проложен к заданию)
file_names = [f"file {i}.txt" for i in range(1, 5)]

# Вызываем функцию read_info для каждого файла по очереди (линейно) измеряя время выполнения с выводом в консоль
start_time = time.time()  # Засекаем время до старта

for file_name in file_names:
    read_info(file_name)  # Вызываем функцию read_info для каждого файла

# Засекаем время после завершения всех вызовов
end_time = time.time()
execution_time_linear = end_time - start_time  # Разница во времени
print(f"Линейное время выполнения: {execution_time_linear:.4f} секунд")

# # Многопроцессное выполнение
# if __name__ == "__main__":
#     start_time = time.time()  # Засекаем время до старта
#
#     with Pool(processes=4) as pool:  # Создаем пул процессов
#         pool.map(read_info, file_names)  # Запускаем функцию read_info для каждого файла
#
#     end_time = time.time()  # Засекаем время после выполнения
#     execution_time_parallel = end_time - start_time  # Разница во времени

#     print(f"Многопроцессное время выполнения: {execution_time_parallel:.4f} секунд")
