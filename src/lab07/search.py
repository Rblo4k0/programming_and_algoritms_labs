def linear_search(nums: list[int], x: int) -> int:
    """Индекс первого вхождения x в списке nums или -1, если элемент не найден.

    Сложность: O(n) по времени, O(1) по памяти.
    """
    for i, value in enumerate(nums):
        if value == x:
            return i
    return -1


def binary_search(sorted_nums: list[int], x: int) -> int:
    """Индекс любого вхождения x в отсортированном по возрастанию списке или -1.

    Важно: список sorted_nums должен быть предварительно отсортирован.
    На неотсортированном списке результат работы функции не определён.
    Сложность: O(log n) по времени, O(1) по памяти.
    """
    lo = 0
    hi = len(sorted_nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def two_sum_brute(nums: list[int], target: int) -> tuple[int, int] | None:
    """Находит пару индексов (i, j), i < j, где nums[i] + nums[j] == target, или None.

    Реализация полным перебором пар.
    Сложность: O(n^2) по времени, O(1) по памяти.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_fast(nums: list[int], target: int) -> tuple[int, int] | None:
    """Находит пару индексов (i, j), i < j, где nums[i] + nums[j] == target, или None.

    Реализация за один проход с помощью словаря (значение -> индекс).
    При наличии нескольких подходящих пар возвращает первую найденную.
    Сложность: O(n) по времени, O(n) по памяти.
    """
    seen: dict[int, int] = {}
    for j, value in enumerate(nums):
        need = target - value
        if need in seen:
            return (seen[need], j)
        if value not in seen:
            seen[value] = j
    return None