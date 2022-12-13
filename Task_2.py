# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            statement = not (x or y or z) == (not x and not y and not z)
            print(
                f'NOT ({x} OR {y} OR {z}) = NOT {x} AND NOT {y} AND NOT {z} -> {statement}')