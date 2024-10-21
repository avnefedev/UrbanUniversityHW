import multiprocessing
from datetime import datetime


def read_info(name):
    all_date = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            str_file = file.readline()
            if str_file:
                all_date.append(str_file)
            else:
                break


files = ['./Files/file 1.txt', './Files/file 2.txt', './Files/file 3.txt', './Files/file 4.txt']

# start = datetime.now()
# for file in files:
#     read_info(file)
# end = datetime.now()
# print(f'Линейный {end - start}')
# Линейный 0:00:03.556504


if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start2 = datetime.now()
        pool.map(read_info, files)
    end2 = datetime.now()
    print(f'Многопроцессорность {end2 - start2}')

# Многопроцессорность 0:00:01.725370



