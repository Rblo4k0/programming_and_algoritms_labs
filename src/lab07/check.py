import random
from src.lab07.search import binary_search, linear_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials: int = 100) -> None:
    """Проверяет функцию сортировки fn против эталонного sorted() на случайных данных."""
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)

        assert result == sorted(original), f"{fn.__name__} ошиблась на {original}: получено {result}"
        assert (nums == original), f"{fn.__name__} изменила исходный список: {nums} != {original}"


def check_search(trials: int = 100) -> None:
    """Проверяет linear_search и binary_search против list.index и оператора in."""

    assert binary_search([], 5) == -1, "binary_search ошибся на пустом списке"
    assert binary_search([5], 5) == 0, "binary_search не нашёл единственный элемент"
    assert binary_search([5], 3) == -1, "binary_search нашёл несуществующий элемент в [5]"
    assert binary_search([1, 3], 1) == 0
    assert binary_search([1, 3], 3) == 1
    assert binary_search([1, 3], 2) == -1
    assert binary_search([1, 3], 5) == -1

    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-50, 50) for _ in range(n)]
        sorted_nums = sorted(nums)

        candidates = nums + [-100, 0, 100, random.randint(-60, 60)]

        for x in candidates:
            # linear_search против list.index
            lin_idx = linear_search(nums, x)
            try:
                expected_idx = nums.index(x)
            except ValueError:
                expected_idx = -1

            assert (lin_idx == expected_idx), f"linear_search({nums}, {x}) -> {lin_idx}, ожидалось {expected_idx}"

            # binary_search на отсортированном списке
            bin_idx = binary_search(sorted_nums, x)
            if x in sorted_nums:
                assert (0 <= bin_idx < len(sorted_nums) and sorted_nums[bin_idx] == x), f"binary_search({sorted_nums}, {x}) вернул неверный индекс {bin_idx}"
            else:
                assert (bin_idx == -1), f"binary_search({sorted_nums}, {x}) -> {bin_idx}, ожидалось -1"


def check_two_sum(trials: int = 100) -> None:
    """Сравнивает two_sum_brute и two_sum_fast на случайных данных и граничных случаях."""
    edge_cases = [
        ([], 0),
        ([5], 10),
        ([3, 3], 6),
        ([3, 2, 4], 6),
        ([2, 7, 11, 15], 9),
        ([1, 2, 3], 10),
    ]

    for nums, target in edge_cases:
        res_brute = two_sum_brute(nums, target)
        res_fast = two_sum_fast(nums, target)
        assert (res_brute is None) == (res_fast is None), f"Расхождение на edge case {nums}, target={target}: brute={res_brute}, fast={res_fast}"

    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-50, 50) for _ in range(n)]

        if n >= 2 and random.random() < 0.5:
            i1, i2 = random.sample(range(n), 2)
            target = nums[i1] + nums[i2]
        else:
            target = random.randint(-100, 100)

        res_brute = two_sum_brute(nums, target)
        res_fast = two_sum_fast(nums, target)

        assert (res_brute is None) == (res_fast is None), f"Расхождение наличия ответа на {nums}, target={target}: brute={res_brute}, fast={res_fast}"

        if res_brute is not None and res_fast is not None:
            i, j = res_brute
            assert (0 <= i < j < n and nums[i] + nums[j] == target), f"two_sum_brute вернул неверные индексы {res_brute} для {nums}, target={target}"

            fi, fj = res_fast
            assert (0 <= fi < fj < n and nums[fi] + nums[fj] == target), f"two_sum_fast вернул неверные индексы {res_fast} для {nums}, target={target}"


def main() -> None:
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn, trials=100)
    check_search(trials=100)
    check_two_sum(trials=100)
    print("OK: 500 проверок (сортировки: 300, поиск: 100, two_sum: 100)")

if __name__ == "__main__":
    main()