# Задача 24:
#     В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
#     В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9

from random import randint

garden_size = int(input("Введите количество кустов: "))
berry_size = int(input("Введите максимальную урожайность с куста: "))
garden_list = dict()

for i in range(0, garden_size):
    garden_list[i] = randint(0, berry_size)
    
    
result_max = 0    #костыль для смыкания окружности
result_max1 = garden_list[len(garden_list)-2] + garden_list[len(garden_list)-1] + garden_list[0]
result_max2 = garden_list[len(garden_list)-1] + garden_list[0] + garden_list[1]
key_max = 0
if result_max1 >= result_max2:
    result_max = result_max1
    key_max = [len(garden_list)-2, len(garden_list)-1, 0]
else :
    result_max = result_max2
    key_max = [len(garden_list)-1, 0, 1]
    
    
for i in range(2, len(garden_list)):
    if result_max < garden_list[i-2] + garden_list[i-1] + garden_list[i]:
        result_max = garden_list[i-2] + garden_list[i-1] + garden_list[i]
        key_max = [i-2, i-1, i]

print(garden_list)
print("С кустов: ", key_max)
print("Максимальное количество ягод за один заход: ", result_max)