# 1. Бинарный поиск (binary search)
#
# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
# my_list = [1, 3, 5, 7, 9]
#
# print(binary_search(my_list, 3))
# print(binary_search(my_list, -1))

# 2. Сортировка выбором (selection sort)
#
# def findSmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
#
# def selectionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr
#
# print(selectionSort([5, 3, 6, 2, 10]))

# 3. Рекурсия (recursion)
# 3.1 Решение задачи с помощью цикла while
#
# def look_for_key(main_box):
#     pile = main_box.make_a_pile_to_look_through()
#     while pile is not None:
#         box = pile.grab_a_box()
#         for item in box:
#             if item.is_a_box():
#                 pile.append(item)
#             elif item.is_a_key():
#                 print("found the key!")

# 3.2 Решение задачи с помощью рекурсии
#
# def look_for_key(box):
#     for item in box:
#         if item.is_a_box():
#             look_for_key(item)
#         elif item.is_a_key():
#             print("found the key!")

# 3.3 Рекурсивный случай: 3...2...1...0...-1...-2...
#
# def countdown(i):
#     print(i)
#     countdown(i - 1)
#
# countdown(3)

# 3.4 Базовый и рекурсивный случаи (base and recursive cases): 3...2...1
#
# def countdown(i):
#     print(i)
#     if i <= 1:
#         return
#     else:
#         countdown(i - 1)
#
# countdown(3)

# 3.5 Стек вызов (call stack)
#
# def greet(name):
#     print("Hello, " + name + "!")
#     greet2(name)
#     print("Getting ready to say bye...")
#     bye()
#
# def greet2(name):
#     print("How are you, " + name + "?")
#
# def bye():
#     print("Ok bye!")
#
# name = input("What is your name? ")
# greet(name)

# 3.6 Стек вызовов с рекурсией
#
# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fact(x - 1)
#
# x = int(input("Enter a number: "))
# print(fact(x))