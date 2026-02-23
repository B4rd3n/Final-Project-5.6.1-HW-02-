# Получение координат крестиков (x), их проверка, а также обновление базы доступных координат и словаря координат крестиков (x)
def x_move():
    while True:
        x_horizontal = int(input("Игрок 1: Координата по горизонтали: "))
        x_vertical = int(input("Игрок 1: Координата по вертикали: "))

        while x_horizontal not in playground.keys() or x_vertical not in playground.get(x_horizontal):
            if any([x_horizontal < 0,
                x_vertical < 0,
                x_horizontal >= field_dimensions,
                x_vertical >= field_dimensions]):
                print("Координата вне поля!\n")
            else:
                print("Эта координата уже занята!\n")
            x_horizontal = int(input("Игрок 1: Координата по горизонтали: "))
            x_vertical = int(input("Игрок 1: Координата по вертикали: "))

        x_coord[x_horizontal].append(x_vertical)
        playground[x_horizontal].remove(x_vertical)
        return

# Получение координат ноликов (о), их проверка, а также обновление базы доступных координат и словаря координат ноликов (о)
def o_move():
    while True:
        o_horizontal = int(input("Игрок 2: Координата по горизонтали: "))
        o_vertical = int(input("Игрок 2: Координата по вертикали: "))

        while o_horizontal not in playground.keys() or o_vertical not in playground.get(o_horizontal):
            if any([o_horizontal < 0,
                o_vertical < 0,
                o_horizontal >= field_dimensions,
                o_vertical >= field_dimensions]):
                print("Координата вне поля!\n")
            else:
                print("Эта координата уже занята!\n")
            o_horizontal = int(input("Игрок 2: Координата по горизонтали: "))
            o_vertical = int(input("Игрок 2: Координата по вертикали: "))

        o_coord[o_horizontal].append(o_vertical)
        playground[o_horizontal].remove(o_vertical)
        return

# Обновление внешнего вида игрового поля
def playground_print():

    for p in range(field_dimensions):
        print(f"\n  {p}", end=" ") if p == 0 else print(p, end=" ")
    print()

    position = 0

    for j in range(field_dimensions):
        amount = 0
        print(position, end=" ")
        position += 1
        while amount < field_dimensions:
            if x_coord_vertical[j].count(amount) == 0 and o_coord_vertical[j].count(amount) == 0:
                print("-", end=" ")
                amount += 1
            else:
                if x_coord_vertical[j].count(amount) != 0:
                    print("x", end=" ")
                else:
                    print("o", end=" ")
                amount += 1
        print()
    print()
    return


# Декоратор на проверку ничьей
def is_draw_decorator(winner):
    def wrapper():

        winner()

        if all(not playground[number] for number in range(field_dimensions)):
            print("Победитель не определён! Ничья!")
            return exit()

    return wrapper


# Проверка победы крестиков (x)
@is_draw_decorator
def is_winner_x():
    winner_count = 0

    # Проверка победы по вертикали
    for k in range(field_dimensions):
        if len(x_coord[k]) == field_dimensions:
            print("Игрок 1: Победа!")
            return exit()

    # Проверка победы по горизонтали
    for n in range (field_dimensions):
        for m in x_coord_vertical:
            winner_count += m.count(n)
            if winner_count == field_dimensions:
                print("Игрок 1: Победа!")
                return exit()
        if winner_count == field_dimensions:
            break
        winner_count = 0

    # Проверка победы по диагонали
    right_diagonal = {step:step for step in range(field_dimensions)}
    left_diagonal = {step:field_dimensions - 1 - step for step in range(field_dimensions)}

    if (all(right_diagonal[item] in x_coord[item] for item in right_diagonal)
            or all(left_diagonal[item] in x_coord[item] for item in left_diagonal)):
        print("Игрок 1: Победа!")
        return exit()

# Проверка победы ноликов (о)
@is_draw_decorator
def is_winner_o():
    winner_count = 0

    # Проверка победы по вертикали
    for k in range(field_dimensions):
        if len(o_coord[k]) == field_dimensions:
            print("Игрок 2: Победа!")
            return exit()

    # Проверка победы по горизонтали
    for n in range (field_dimensions):
        for m in o_coord_vertical:
            winner_count += m.count(n)
            if winner_count == field_dimensions:
                print("Игрок 2: Победа!")
                return exit()
        if winner_count == field_dimensions:
            break
        winner_count = 0

    # Проверка победы по диагонали
    right_diagonal = {step:step for step in range(field_dimensions)}
    left_diagonal = {step:field_dimensions - 1 - step for step in range(field_dimensions)}

    if (all(right_diagonal[item] in o_coord[item] for item in right_diagonal)
            or all(left_diagonal[item] in o_coord[item] for item in left_diagonal)):
        print("Игрок 2: Победа!")
        return exit()





# Приветствие и выбор размеров игрового поля
print('Итоговое задание "Крестики-Нолики"\n')
options = {"1" : 3, "2" : 5, "3" : 7}
field_dimensions = input("Возможные размеры игрового поля \n1. 3x3 \n2. 5x5 \n3. 7x7 \n\nВпишите номер выбора: ")

while field_dimensions not in options:
    print("Такого варианта не существует!\n")
    field_dimensions = input("Сделайте выбор ещё раз: ")

field_dimensions = options[field_dimensions]



# Печать пустого игрового поля
for i in range(field_dimensions):
    print(f"\n  {i}", end=" ") if i == 0 else print(i, end=" ")
print()
for i in range(field_dimensions):
    print(i, end=" ")
    print("- " * field_dimensions)
print()



# Создание базы доступных для игры координат
playground = {i: [] for i in range(field_dimensions)}
for i in playground.values():
    count = 0
    while len(i) < field_dimensions:
        i.append(count)
        count += 1


# Создание словаря для записи координат крестиков (x)
x_coord = {i: [] for i in range(field_dimensions)}
x_coord_vertical = list(x_coord.values())

# Создание словаря для записи координат ноликов (о)
o_coord = {i: [] for i in range(field_dimensions)}
o_coord_vertical = list(o_coord.values())


# Выполнение программы
while True:
    x_move()
    playground_print()
    is_winner_x()

    o_move()
    playground_print()
    is_winner_o()
