#Волохов Дмитрий
#1. Создать программно файл в текстовом формате, 
#записать в него построчно данные, 
#вводимые пользователем. 
#Об окончании ввода данных свидетельствует пустая строка.

try:
    with open('HW_5_1.txt', 'w') as us_file:
        us = True
        while us == True:
            us_str = input('>>>')
            if us_str == '':
                break
            else:
                print(us_str, file = us_file )
            
         
except IOError as err:
    print(err)

#2. Создать текстовый файл (не программно), 
#сохранить в нем несколько строк, 
#выполнить подсчет количества строк, 
#количества слов в каждой строке.

lines = 0

try:
    with open('HW_5_2.txt', 'r') as us_file:
        for line in us_file:
            lines += 1  
            words = 0
            for word in line:
                words += 1
                
            print(f'В {lines} строке:  {words} слов(а)')
        
except IOError as err:
    print(err) 

print(f'Всего {lines} строк') 


#3. Создать текстовый файл (не программно), 
#построчно записать фамилии сотрудников и величину их окладов. 
#Определить, кто из сотрудников имеет оклад менее 20 тыс., 
#вывести фамилии этих сотрудников. 
#Выполнить подсчет средней величины дохода сотрудников.

try:
    with open('HW_5_3.txt', 'r') as us_file:
        all_rate = []
        min_rate = []
        for line in us_file:
            i = line.split()
            if int(i[1]) < 20000:
                min_rate.append(i[0])
            all_rate.append(i[1])
           
except IOError as err:
    print(err)
print(f'Меньше 20к: {min_rate}')
print(f'Средняя зарплата:{sum(map(int, all_rate)) / len(all_rate)}')
   
    
#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, 
#открывающую файл на чтение и считывающую построчно данные. 
#При этом английские числительные должны заменяться на русские. 
#Новый блок строк должен записываться в новый текстовый файл.

abble = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
file_new =[]

with open('HW_5_4.txt', 'r') as us_file:
    for i in us_file:
        i = i.split(' ', 1)
        file_new.append(abble[i[0]] + ' ' + i[1])
    
    
with open('HW_5_4new.txt', 'w') as new_file:
    new_file.writelines(file_new)
        




#5. Создать (программно) текстовый файл, 
#записать в него программно набор чисел, 
#разделенных пробелами. 
#Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

try:
    with open('HW_5_5.txt', 'w') as us_file:
        num = input('Введите цифры через пробел:  ')
        us_file.writelines(num)
        my_num = num.split()

        print(sum(map(int, my_num)))
except IOError:
    print('Ошибка в файле')
except ValueError:
    print('Ошибка ввода-вывода')

#6. Необходимо создать (не программно) текстовый файл, 
#где каждая строка описывает учебный предмет и наличие лекционных, 
#практических и лабораторных занятий по этому предмету и их количество. 
#Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
#Сформировать словарь, 
#содержащий название предмета и общее количество занятий по нему. 
#Вывести словарь на экран.
#Примеры строк файла:

#Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря:

#{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

subj = {}
with open('HW_5_6.txt', 'r') as us_file:
    
    for line in us_file:
        new_line = line.replace("—", "0")
        new_line = new_line.replace("(л)", "")
        new_line = new_line.replace("(пр)", "")
        new_line = new_line.replace("(лаб)", "")
        new_line = new_line.replace(".", "")
        

        subject, lecture, practice, lab = new_line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее часы по предмету - \n {subj}')

#7. Создать (не программно) текстовый файл, 
#в котором каждая строка должна содержать данные о фирме: 
#название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, 
#вычислить прибыль каждой компании, 
#а также среднюю прибыль. 
#Если фирма получила убытки, 
#в расчет средней прибыли ее не включать.
#Далее реализовать список. 
#Он должен содержать словарь с фирмами и их прибылями, 
#а также словарь со средней прибылью. 
#Если фирма получила убытки, 
#также добавить ее в словарь (со значением убытков).
#Пример списка: 
#[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:

#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджеры контекста.
import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('HW_5_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Средняя прибыль - {prof_aver:.2f}')
    else:
        print('Средняя прибыль - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print('Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}') 