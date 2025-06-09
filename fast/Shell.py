# def shell_sort(arr):
#     n = len(arr)
#     gap = n // 2
#
#     while gap > 0:
#         for i in range(gap, n):
#             temp = arr[i]
#             j = i
# 
#             while j >= gap and arr[j - gap] > temp:
#                 arr[j] = arr[j - gap]
#                 j -= gap
#             arr[j] = temp
#         gap //= 2
#     return arr


def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Начальный интервал
    print(f'{gap} начальный индекс интервал (в списке это элемент {arr[gap]})')

    while gap > 0:
        print(f'Цикл начинается с середины списка gap = {gap} и идёт до конца списка n(len(arr)) = {n}')
        for i in range(gap, n):
            print(f'\tБерём первый номер i = {i}')
            temp = arr[i]
            print(f'\tЗаписали его значение в temp: temp = arr[{i}] = {temp}')
            j = i
            print(f'\tВ переменную j записываем индекс первого элемента:  j = i = {j}')

            print(f'\tЗаходим/нет в while')
            print(f'\tПервое условие: j >= gap - {j >= gap}')
            print(f'\tВторое условие: arr[j - gap] > temp - {arr[j - gap] > temp}')
            while j >= gap and arr[j - gap] > temp:

                print('\t\tЗашли')
                print(f'\t\tНа место arr[j] = arr[{j}] (второй элемент) записываем arr[j - gap] = arr[{j} - {gap}] (значение первого элемента)')
                print(f'\t\tто есть на место arr[{j}] = {arr[j]} записываем arr[{j - gap}] = {arr[j - gap]}')
                arr[j] = arr[j - gap]
                print(arr)

                print(f'\t\tПереписываем j -= gap (j = {j} - {gap} = {j - gap})')
                j -= gap

                print(f'\tПервое условие: j >= gap - {j >= gap}')
                print(f'\tВторое условие: arr[j - gap] > temp - {arr[j - gap] > temp}')

            arr[j] = temp
            print(f'\tarr[j] = temp, где j = {j} (индекс первого элемента - gap), temp = {temp} (значение элемента arr[i], которое сохранили)')
            print(f'\tТеперь в arr[{j}] лежит {arr[j]}')
            print(arr)

        gap //= 2  # Уменьшаем интервал
        print(f'Уменьшаем интервал gap //= 2 = {gap}')
    return arr


# Пример использования
arr = [12, 34, 54, 2, 3, 9, 8, -5, 0, 100]
sorted_arr = shell_sort(arr)
print("Отсортированный массив:", sorted_arr)