# #_author_ Подрезов Евгений Владимирович
import math
import random

fruit = ["яблоко", "банан", "киви", "арбуз"]
last_name = len(fruit)
for i in range(last_name):
    print(str(i+1) + "." + "{}".format(fruit[i]))


one_list = [1, 6, 5, 7, 8, 9, 10]
two_list = [1, 5, 7, 9]
for i in two_list:
    if i in one_list:
        one_list.remove(i)
print(one_list)
print(two_list)



first_list = [1, 2, 5, 8, 10, 15, 18]
new_list = []
last_name = len(first_list)
for i in range(last_name):
    if first_list[i] % 2 == 0:
        new_list.append(first_list[i]/4)
    else:
        new_list.append(first_list[i]*2)
        print(new_list)


one_list = [-5, 7, 8, 15, 25, -15, -36]
new_list = []
for item in one_list:
    if item > 0 and math.sqrt(item) % 1 == 0:
        new_list.append(int(math.sqrt(item)))
print(new_list)


dana_data = "18.12.1990"
data_list = dana_data.split('.')
dict_months = {
"01" : "января",
"02" : "Февраля",
"03" : "марта",
"04" : "апреля",
"05" : "мая",
"06" : "июня",
"07" : "июля",
"08" : "августа",
"09" : "сентября",
"10" : "октября",
"11" : "ноября",
"12" : "декабря"
}

dict_days = {
"01" : "первое", "02" : "второе", "03" : "третье", "04" : "четвертое","05" : "пятое", "06" : "шестое",
"07" : "седьмое", "08" : "восьмое","09" : "девятое", "10" : "десятое","11" : "одиннадцатое",
"12" : "двенадцатое", '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое',
'16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое',
'21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвёртое',
'25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое',
'29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое'
}
for key in dict_days:
    if data_list[0] == key:
        data_list[0] = dict_days[key]

for key in dict_months:
    if data_list[1] == key:
        data_list[1] = dict_months[key]

answer_data = data_list[0] + ' ' + data_list[1] + ' ' + data_list[2] + ' ' "года"
print(answer_data)

n = int(input('введите количество случайных элементов в списке: '))
my_list = []
for el in range(n):
    my_list.append(random.randint(-100, 100))
print(my_list)


one_list = [1, 2, 5, 6, 7, 5, 3, 1]
new_list = set(one_list)
print(new_list)

