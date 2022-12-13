# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('\nВведите номер четверти: '))

if quarter < 1 or quarter > 4:
  print(f'\n{quarter}-ая четверть не существует')
elif quarter == 1:
  print(f'\nЕсли номер четверти = {quarter} -> X > 0 и Y > 0')
elif quarter == 2:
  print(f'\nЕсли номер четверти = {quarter} -> X < 0 и Y > 0')
elif quarter == 3:
  print(f'\nЕсли номер четверти = {quarter} -> X < 0 и Y < 0')
else:
  print(f'\nЕсли номер четверти = {quarter} -> X > 0 и Y < 0')