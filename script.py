import sys


# Проверка, введено ли именно число
def try_expect(integer):
    while True:
        value = input(integer)
        if value.isdigit():
            return int(value)
        else:
            print("\nОшибка ввода! Нужно ввести целое число.\n")

# Получение координат, их проверка, а также обновление базы доступных координат и словаря координат
def move(field: dict, coords: dict, player):
    while True:
        horizontal = try_expect(f"Игрок {player}: Координата по горизонтали: ")
        vertical = try_expect(f"Игрок {player}: Координата по вертикали: ")

        while horizontal not in field.keys() or vertical not in field.get(horizontal):

            if any([horizontal < 0,
                vertical < 0,
                horizontal >= field_dimensions,
                vertical >= field_dimensions]):
                print("\nКоордината вне поля!\n")
            else:
                print("\nЭта координата уже занята!\n")

            horizontal = try_expect(f"Игрок {player}: Координата по горизонтали: ")
            vertical = try_expect(f"Игрок {player}: Координата по вертикали: ")

        coords[horizontal].append(vertical)
        field[horizontal].remove(vertical)
        return

# Обновление внешнего вида игрового поля
def playground_print(x_v, o_v):

    for p in range(field_dimensions):
        print(f"\n  {p}", end=" ") if p == 0 else print(p, end=" ")
    print()

    position = 0

    for j in range(field_dimensions):
        amount = 0
        print(position, end=" ")
        position += 1
        while amount < field_dimensions:
            if x_v[j].count(amount) == 0 and o_v[j].count(amount) == 0:
                print("-", end=" ")
                amount += 1
            else:
                if x_v[j].count(amount) != 0:
                    print("x", end=" ")
                else:
                    print("o", end=" ")
                amount += 1
        print()
    print()
    return


# Декоратор на проверку ничьей
def is_draw_decorator(winner):
    def wrapper(*args, **kwargs):

        winner(*args, **kwargs)

        if all(not args[2][number] for number in range(field_dimensions)):
            print("Победитель не определён! Ничья!")
            sys.exit()

    return wrapper


# Проверка победы
@is_draw_decorator
def is_winner(coord: dict, coords_v, field: dict, player):
    winner_count = 0

    # Проверка победы по вертикали
    for k in range(field_dimensions):
        if len(coord[k]) == field_dimensions:
            print(f"Игрок {player}: Победа!")
            sys.exit()

    # Проверка победы по горизонтали
    for n in range (field_dimensions):
        for m in coords_v:
            winner_count += m.count(n)
            if winner_count == field_dimensions:
                print(f"Игрок {player}: Победа!")
                sys.exit()
        if winner_count == field_dimensions:
            break
        winner_count = 0

    # Проверка победы по диагонали
    right_diagonal = {step:step for step in range(field_dimensions)}
    left_diagonal = {step:field_dimensions - 1 - step for step in range(field_dimensions)}

    if (all(right_diagonal[item] in coord[item] for item in right_diagonal)
            or all(left_diagonal[item] in coord[item] for item in left_diagonal)):
        print(f"Игрок {player}: Победа!")
        sys.exit()


# Приветствие и выбор размеров игрового поля
print('Итоговое задание "Крестики-Нолики".\n')
options = {"1" : 3, "2" : 5, "3" : 7}
field_dimensions = input("Возможные размеры игрового поля \n1. 3x3 \n2. 5x5 \n3. 7x7 \n\nВпишите номер выбора: ")

while field_dimensions not in options:
    print("Такого варианта не существует!\n")
    field_dimensions = input("Сделайте выбор ещё раз: ")

field_dimensions = options[field_dimensions]

# Нумерация игроков
x = 1
o = 2


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

# Печать пустого игрового поля
playground_print(x_coord_vertical, o_coord_vertical)


# Выполнение программы
while True:
    move(playground, x_coord, x)
    playground_print(x_coord_vertical, o_coord_vertical)
    is_winner(x_coord, x_coord_vertical, playground, x)

    move(playground, o_coord, o)
    playground_print(x_coord_vertical, o_coord_vertical)
    is_winner(o_coord, o_coord_vertical, playground, o)
