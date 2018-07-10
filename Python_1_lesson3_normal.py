__author__ = 'Герман Дмитрий Юрьевич'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):

    my_list = [1, 1]
    for i in range(m - 2):
        my_list.append(my_list[i] + my_list[i + 1])
    for j in range(n - 1):
        del my_list[0]
    print(my_list)

fibonacci(8, 14)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):

    my_list = []
    for i in range(len(origin_list)):
        my_list.append(min(origin_list))
        del origin_list[origin_list.index(min(origin_list))]
    origin_list = my_list
    print(origin_list)

sort_to_max([2,10,-12,2.5,20,-11,4,4,0])


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_1(arg,my_list):

    list_1 = []
    for i in my_list:
        if i != arg:
            list_1.append(i)
    print(list_1)
    
filter_1(1,[1, 2, 3, 4, 1, 1, 5, 6, 7, 1, 8, 9, 1, 1])

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parallel(x1, y1, x2, y2):

    return x1 * y2 - y1 * x2 == 0 

def my_parallelogram(x1, y1, x2, y2, x3, y3, x4, y4):

    return (parallel(x2 - x1, y2 - y1, x3 - x4, y3 - y4) \
    and parallel(x3 - x2, y2 - y3, x4 - x1, y4 - y1)) \
    or (parallel(x3 - x1, y3 - y1, x2 - x4, y2 - y4) \
    and parallel(x2 - x3, y2 - y3, x1 - x4, y1 - y4))

print(my_parallelogram(0, 0, 1, 1, 2, 1, 1, 0))


