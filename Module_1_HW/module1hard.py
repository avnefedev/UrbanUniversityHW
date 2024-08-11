grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
grades_average = [sum(i)/len(i) for i in grades]

dict = {students_list[i]: grades_average[i] for i in range(len(students_list))}
print(dict)
