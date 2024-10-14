def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])  # Знайшли точний збіг

        if arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    # Якщо не знайдено точний збіг, повертаємо найменший елемент, більший або рівний target
    return (iterations, upper_bound)


# Тестуємо функцію
sorted_array = [0.1, 1.5, 2.7, 3.3, 5.5, 6.8, 8.0, 9.4]
target_value = 4.0

result = binary_search(sorted_array, target_value)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")
