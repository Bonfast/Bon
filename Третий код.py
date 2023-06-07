def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid

    return left

sequence = input("Введите последовательность чисел через пробел: ")
target = input("Введите любое число: ")

try:
    sequence = list(map(int, sequence.split()))
    target = int(target)
except ValueError:
    print("Ошибка ввода. Проверьте правильность введенных данных.")
    exit()

sorted_sequence = sorted(sequence)
position = binary_search(sorted_sequence, target)

if position >= len(sorted_sequence):
    print("Введенное число больше всех чисел в последовательности.")
else:
    print(f"Позиция вставки числа {target}: {position}")
