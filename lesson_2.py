#Волохов Дмитрий
#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. 
#Использовать функцию type() для проверки типа. 
#Элементы списка можно не запрашивать у пользователя, а указать явно,
# в программе.
my_list = [55, 6.2, True, 'geek', [4,6], None, {7: 'oktober', 8: 'november'}]

for i, item in enumerate(my_list, 1):
    print(f'{i}. {item} - {type(item)}')

#2. Для списка реализовать обмен значений соседних элементов, т.е. 
#Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
#При нечетном количестве элементов последний сохранить на своем месте. 
#Для заполнения списка элементов необходимо использовать функцию input().
number = input('Введите числа:  ')
while not number.isdigit():
    number = input("Это не число: ")
my_list = list(number)
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i-1]
    
print(my_list)

#3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
#Напишите решения через list и через dict.
while True:
    month_user = input('Введите номер месяца:  ')
    if month_user.isdigit() and 0 < int(month_user) <= 12:
        season_list = ["зима","весна","лето","осень","зима"]
        season_dict = {0: "зима", 1: "весна", 2: "лето", 3: "осень", 4: "зима"}
        print(f'Список:  {season_list[int(month_user) // 3]}\nСловарь: {season_dict[int(month_user) // 3]}')
        break
    elif month_user == 'exit':
        break
    else:
        print('Ошибка')

#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
#Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
#Если в слово длинное, выводить только первые 10 букв в слове.
str_user = input("Введите текст:  ")
my_word = []
num = 1
for el in range(str_user.count(' ') + 1):
    my_word = str_user.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [el]}")
        num += 1
    else:
        print(f" {num} {my_word [el] [0:10]}")
        num += 1

#5. Реализовать структуру «Рейтинг», 
#представляющую собой не возрастающий набор натуральных чисел. 
#У пользователя необходимо запрашивать новый элемент рейтинга. 
#Если в рейтинге существуют элементы с одинаковыми значениями, 
#то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
number = input("Введите число: ")
while not number.isdigit():
    number = input("Это не число(31415 - выход): ")
num_user = int(number)
while num_user != 31415:
    for el in range(len(my_list)):
        if my_list[el] == num_user:
            my_list.insert(el + 1, num_user)
            break
        elif my_list[0] < num_user:
            my_list.insert(0, num_user)
        elif my_list[-1] > num_user:
            my_list.append(num_user)
        elif my_list[el] > num_user and my_list[el + 1] < num_user:
            my_list.insert(el + 1, num_user)
    print(f"текущий список - {my_list}")
    print(f"Рейтинг - {my_list}")
    number = input("Введите число: ")
    while not number.isdigit():
        number = input("Это не число(31415 - выход): ")
    num_user = int(number)


#6. * Реализовать структуру данных «Товары». 
#Она должна представлять собой список кортежей. 
#Каждый кортеж хранит информацию об отдельном товаре. 
#В кортеже должно быть два элемента — номер товара и словарь с параметрами 
#(характеристиками товара: название, цена, количество, единица измерения). 
#Структуру нужно сформировать программно, 
#т.е. запрашивать все данные у пользователя.

goods = []
features = {'Название': '', 'Цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'Название': [], 'Цена': [], 'количество': [], 'единица измерения': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Выход 'Q', для продолжения нажмите кнопку 'Enter', Аналитика 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Текущая аналитика \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Введите "{f}": ')
        features[f] = int(feature_) if (f == 'Цена' or f == 'количество') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))







