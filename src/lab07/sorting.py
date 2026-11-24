def bubble_sort(nums: list[int]) -> list[int]:
    """Возвращает новый отсортированный по возрастанию список (сортировка пузырьком).

    Исходный список не изменяется.
    Включает флаг раннего выхода, если за проход не было ни одного обмена.
    Сложность: O(n^2) в худшем/среднем случае, O(n) на отсортированном списке.
    """
    arr = list(nums)
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


def insertion_sort(nums: list[int]) -> list[int]:
    """Возвращает новый отсортированный по возрастанию список (сортировка вставками).

    Исходный список не изменяется.
    Сложность: O(n^2) в худшем/среднем случае, O(n) на почти отсортированных данных.
    """
    arr = list(nums)

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def selection_sort(nums: list[int]) -> list[int]:
    """Возвращает новый отсортированный по возрастанию список (сортировка выбором).

    Исходный список не изменяется.
    Сложность: O(n^2) во всех случаях (всегда ~n^2/2 сравнений).
    """
    arr = list(nums)
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr