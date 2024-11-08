import matplotlib.pyplot as plt
import requests
import pandas as pd

# res1 = requests.get('https://urban-university.ru/')
#
# print(res1.headers)
# print(res1.status_code)
# print(res1.encoding)
# print(res1.text)

# example = pd.Series([1, 3, 4, 5])
# school = {'Ученик': ['Петя', 'Вася', 'Саша', 'Таня'],
#             'Оценка за четверть': [3, 4, 5, 3],
#             'Оценка за год': [4, 4, 5, 4]}
# dates = pd.date_range('20240811', periods=5)
# df = pd.DataFrame(school)
# print(example)
# print(df)
# print(dates)
# print(df.dtypes)
# print(df.describe())

# y = [i for i in range(10)]
# x = [i**2 for i in y]
#
# plt.plot(y, x, color='red', marker='X', markersize=6)
# plt.xlabel('Ось Х')
# plt.ylabel('Ось Y')
# plt.title('График')
# plt.show()

vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]
plt.pie(vals, labels=labels)
plt.title("Распределение марок автомобилей на дороге")
plt.show()
