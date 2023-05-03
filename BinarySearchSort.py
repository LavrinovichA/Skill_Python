def binary_search(lst, x):
    """Функция для двоичного поиска элемента x в отсортированном списке lst"""
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left


def sort_list(lst):
    """Функция для сортировки списка lst"""
    return sorted(lst)


# Ввод последовательности чисел
input_str = input("Введите последовательность чисел через пробел: ")
lst = input_str.split()

# Проверка соответствия ввода
if not all(map(str.isdigit, lst)):
    print("Ошибка: в последовательности есть нечисловые значения")
    exit()

# Ввод числа для поиска
num = input("Введите число для поиска: ")
if not num.isdigit():
    print("Ошибка: введено нечисловое значение")
    exit()
num = int(num)

# Преобразование введенной последовательности в список и сортировка
lst = sort_list(list(map(int, lst)))

# Поиск номера позиции элемента в списке
pos = binary_search(lst, num)

# Вывод результата
if pos >= len(lst):
    print(f"Введенное число {num} больше всех элементов в последовательности")
elif lst[pos] == num:
    print(f"Введенное число {num} находится на позиции {pos}")
else:
    print(f"Введенное число {num} находится между позициями {pos-1} и {pos} и между элементами {lst[pos-1]} и {lst[pos]}")
