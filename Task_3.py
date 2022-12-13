# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('\nВведите значание X: '))
y = int(input('Введите значение Y: '))

if x == 0 or y == 0:
    print(f'\nЗначения X = {x} и Y = {y} не соответствуют условию задачи!')
elif x > 0 and y > 0:
  print(f'\nx = {x}; y = {y} -> 1')
elif x < 0 and y > 0:
  print(f'\nx = {x}; y = {y} -> 2')
elif x < 0 and y < 0:
  print(f'\nx= {x}; y = {y} -> 3')
else:
  print(f'\nx = {x}; y = {y} -> 4')