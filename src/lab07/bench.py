from pathlib import Path
import random
import timeit
from src.lab04.io_txt_csv import write_csv
from src.lab07.search import binary_search, linear_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def bench_sorts() -> list[tuple[str, int, str, str]]:
    """Замер времени работы сортировок на n = 1_000, 10_000, 100_000."""
    rows: list[tuple[str, int, str, str]] = []
    sizes = [1_000, 10_000, 100_000]

    algorithms = [
        ("sorted", sorted, False),
        ("bubble_sort", bubble_sort, True),
        ("insertion_sort", insertion_sort, True),
        ("selection_sort", selection_sort, True),
    ]

    for n in sizes:
        random.seed(42)
        data = [random.randint(-100_000, 100_000) for _ in range(n)]

        for name, fn, is_quadratic in algorithms:
            if is_quadratic and n >= 100_000:
                rows.append(("sort", n, name, "> 60"))
                continue

            repeats = 5 if n == 1_000 else 1
            t = timeit.timeit(lambda: fn(data), number=repeats) / repeats
            rows.append(("sort", n, name, f"{t:.6f}"))

    return rows


def bench_search() -> list[tuple[str, int, str, str]]:
    """Замер поиска: 10 000 случайных запросов к списку из 100 000 элементов."""
    rows: list[tuple[str, int, str, str]] = []
    n = 100_000
    num_queries = 10_000

    random.seed(42)
    data = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]
    queries = [
        data[random.randint(0, n - 1)]
        if i % 2 == 0
        else random.randint(-1_500_000, 1_500_000)
        for i in range(num_queries)
    ]

    # 1. Линейный поиск (10 000 запросов)
    t_linear = timeit.timeit(lambda: [linear_search(data, q) for q in queries], number=1)
    rows.append(("search", n, "linear_search", f"{t_linear:.6f}"))

    # 2. Предварительная сортировка + бинарный поиск (10 000 запросов)
    t_sort = timeit.timeit(lambda: sorted(data), number=1)
    sorted_data = sorted(data)

    t_binary = timeit.timeit(lambda: [binary_search(sorted_data, q) for q in queries], number=1)
    rows.append(("search", n, "binary_search", f"{t_binary:.6f}"))
    rows.append(("search", n, "sorted + binary_search", f"{t_sort + t_binary:.6f}"))

    return rows


def bench_two_sum() -> list[tuple[str, int, str, str]]:
    """Замер two_sum_brute и two_sum_fast на n = 1_000, 10_000."""
    rows: list[tuple[str, int, str, str]] = []
    sizes = [1_000, 10_000]

    for n in sizes:
        random.seed(42)
        data = [random.randint(-1_000_000_000, 1_000_000_000) for _ in range(n)]
        target = data[-2] + data[-1]

        t_brute = timeit.timeit(lambda: two_sum_brute(data, target), number=1)
        rows.append(("two_sum", n, "two_sum_brute", f"{t_brute:.6f}"))

        repeats_fast = 100
        t_fast = (timeit.timeit(lambda: two_sum_fast(data, target), number=repeats_fast) / repeats_fast)
        rows.append(("two_sum", n, "two_sum_fast", f"{t_fast:.6f}"))

    return rows


def print_table(rows: list[tuple[str, int, str, str]]) -> None:
    """Выводит аккуратную таблицу замеров в консоль."""
    header = f"{'task':<10} | {'n':>8} | {'impl':<24} | {'seconds':>12}"
    print(header)
    print("-" * len(header))
    for task, n, impl, seconds in rows:
        print(f"{task:<10} | {n:>8} | {impl:<24} | {seconds:>12}")


def main() -> None:
    all_rows: list[tuple[str, int, str, str]] = []
    all_rows.extend(bench_sorts())
    all_rows.extend(bench_search())
    all_rows.extend(bench_two_sum())

    print_table(all_rows)

    out_path = Path("data/lab07/bench.csv")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    write_csv(all_rows, out_path, header=("task", "n", "impl", "seconds"))
    print(f"\nРезультаты сохранены в {out_path}")


if __name__ == "__main__":
    main() 